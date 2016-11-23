import json
import pprint
import re
import sys
import urllib
import uuid

import vkontakte
from django.conf import settings
from django.contrib.auth import login
from django.contrib.auth import logout
from django.core.files.base import ContentFile
from django.core.files.storage import default_storage
from django.core.mail import EmailMessage
from django.http import HttpResponse
from django.shortcuts import redirect
from django.shortcuts import render

from Users.calculations import calculatecalories
from Users.models import User
from .forms import LoginForm, RegisterForm, AccountForm


def index(request):
    resp = "<h1>List of latest users</h1><hr>"
    latest_users = User.objects.order_by('-pk')[:100]

    us = []

    for u in latest_users:
        pu = u.photourl
        
        if (pu and not pu.startswith('http')):
            pu = settings.DOMAIN + '/' + pu
        
        if pu:
            us.extend([{'first': u.first_name, 'last': u.last_name, 'id': u.id, 'photourl':pu,
                        
                        'start_weight':u.start_weight,
                        'current_weight':u.current_weight,
                        'goal_weight': u.goal_weight                       
                        } ])
            
    return render(request, 'allusers.html', {'us':us})

def index_old(request):
    resp = "<h1>List of latest users</h1><hr>"
    latest_users = User.objects.order_by('-pk')[:100]
    output = '<br> '.join([u.username for u in latest_users])
    resp = resp + "<br>" + output + "<hr>"
    return HttpResponse(resp)


def customlogout(request):
    if request.user.is_authenticated():
        logout(request)

    return redirect('/')

def customlogin(request):

    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = LoginForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required

            the_username = request.POST.get('username', False)
            the_password = request.POST.get('password', False)

            if settings.DEBUG:
                print >>sys.stderr, "Got login and password: "
                print >>sys.stderr, the_username
                print >>sys.stderr, the_password
                print >>sys.stderr, pprint.pprint(form)

            try:
                user = User.objects.get(username=the_username)

                #user = authenticate(username=username, password=password)
                if (user is not None) and (user.password == the_password):
                    login(request, user)
                    # Redirect to a success page.
                    return redirect('/')
                else:
                    # Return an 'invalid password' error message.
                    form.invalid = 2

            except Exception:
                # Return an 'invalid login' error message.
                form.invalid=1



    # if a GET (or any other method) we'll create a blank form
    else:
        form = LoginForm()

    return render(request, 'registration/login.html', {'form' : form})

def customregister(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:

        formreg = RegisterForm(request.POST)
        # check whether it's valid:
        if formreg.is_valid():
            # process the data in form.cleaned_data as required

            username = request.POST.get('username', False)
            email = request.POST.get('email', False)
            password = request.POST.get('password', False)
            password_repeat = request.POST.get('password_repeat', False)

            if settings.DEBUG:
                print >> sys.stderr, "Got login, email and password: "
                print >> sys.stderr, pprint.pprint(formreg)
            if User.objects.filter(email=email).exists():
                formreg.invalid = 3
            else:
                if User.objects.filter(username=username).exists():
                    formreg.invalid = 2
                else:
                    if password == password_repeat:
                        form = LoginForm(request.POST)
                        user = User(username=username, password=password, email=email)
                        user.save()
                        subject = 'Thank you for InstoKilogram registration'
                        message = 'Welcome to InstoKilogram!/n' \
                                  'To finish registration, please proceed the following link./n' \
                                  'If you did not register at our site, please ignore this message./n' \
                                  '/n' \
                                  'Yours,' \
                                  'InstoKilogram'
                        from_email = settings.EMAIL_HOST_USER
                        to_list = [email]
                        email_confirm = EmailMessage(
                            subject,
                            message,
                            to_list,
                        )
                        email_confirm.send()
                        #send_mail(subject, message, from_email, to_list, fail_silently=True)
                        if user is not None:
                            login(request, user)
                            # Redirect to a success page.
                            return redirect('/')
                        else:
                            # Return an 'invalid login' error message.
                            if 1:
                                form.invalid = 1
                            # User is inactive
                            else:
                                form.invalid = 2
                    else:
                        formreg.invalid = 1

    else:
        formreg = RegisterForm()

    return render(request, 'registration/register_form.html', {'form': formreg})


def accountsprofile(request):
    if (not request.user.is_authenticated()):
        return redirect('/')

    current_user = request.user
    # current_profile = request.userprofile

    status = 0

    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = AccountForm(request.POST, request.FILES)

        for error in form.errors:
            print>>sys.stderr, error
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required

            the_firstname = request.POST.get('firstname', False)
            the_lastname = request.POST.get('lastname', False)
            gender = request.POST.get('gender', False)
            start_weight = request.POST.get('start_weight', False)
            height = request.POST.get('height', False)
            birth_date = form.cleaned_data.get('birth_date', False)
            activity_level = request.POST.get('activity_level', False)
            diet_goals = request.POST.get('diet_goals', False)
            goal_weight = request.POST.get('goal_weight', False)
            image = form.cleaned_data['image']

            if settings.DEBUG:
                print >> sys.stderr, "Got data: "
                print >> sys.stderr, pprint.pprint(image)

            try:
                user = User.objects.get(username=current_user.username)
                user.first_name = the_firstname
                user.last_name = the_lastname
                user.gender = gender
                user.start_weight = start_weight
                user.height = height
                user.birth_date = birth_date
                user.activity_level = activity_level
                user.diet_goals = diet_goals
                user.goal_weight = goal_weight
                user.calories = calculatecalories(gender, start_weight, height, birth_date, activity_level)

                file_name = 'avatar/' + current_user.username + '/' + image.name
                path = default_storage.save(file_name, ContentFile(image.read()))
                user.photourl = "/media/" + path

                user.save()

                status = 1

                current_user = user
            except Exception as e:
                # Return an 'invalid login' error message.
                print >> sys.stderr, e
                status = 2

    # if a GET (or any other method) we'll create a blank form

    data = {'firstname': current_user.first_name,
            'lastname': current_user.last_name,
            'email': current_user.email,
            'username': current_user.username,
            'gender': current_user.gender,
            'start_weight': current_user.start_weight,
            'height': current_user.height,
            'birth_date': current_user.birth_date,
            'activity_level': current_user.activity_level,
            'diet_goals': current_user.diet_goals,
            'goal_weight': current_user.goal_weight,
            'image': current_user.photourl,
            }
    user = current_user

    form = AccountForm(data)

    return render(request, 'registration/profile.html', {'form': form, 'status': status, 'data': data, 'user': user})


def vklogin_widget(request):
    first_name = request.GET.get('first_name', False)
    last_name  = request.GET.get('last_name', False)
    photo = request.GET.get('photo', False)

    if settings.DEBUG:
        print >>sys.stderr, "Got VK data: "
        print >>sys.stderr, pprint.pprint(first_name)

    return render(request, 'registration/vklogin.html', {'first_name' : first_name, 'last_name' : last_name, 'photo' : photo})


def vkoauth(request):
    redirect_url = settings.VK_REDIR

    auth_url = "https://oauth.vk.com/authorize?client_id=" + str(settings.VK_CLIENT_ID) + "&scope=" + settings.VK_SCOPE
    auth_url = auth_url + "&redirect_uri=" + urllib.pathname2url(redirect_url)
    auth_url = auth_url + "&display=page&v=5.9&response_type=code"

    if settings.DEBUG:
        print >>sys.stderr, "Auth URL: "
        print >>sys.stderr, pprint.pprint(auth_url)

    return redirect(auth_url)


def vkoauthcb(request):
    code  = request.GET.get('code', False)
    error_description = request.GET.get('error_description')

    if (not code) or (error_description):
        return redirect('/vklogin/?error_description=' + error_description)

    redirect_url = settings.VK_REDIR

    auth_url = "https://oauth.vk.com/access_token?client_id=" + str(settings.VK_CLIENT_ID) + "&scope=" + settings.VK_SCOPE
    auth_url = auth_url + "&client_secret=" + str(settings.VK_CLIENT_SECRET)
    auth_url = auth_url + "&redirect_uri=" + urllib.pathname2url(redirect_url)
    auth_url = auth_url + "&code=" + str(code)

    response = urllib.urlopen(auth_url)
    data = json.loads(response.read())

    access_token = data.get('access_token')
    user_id = data.get('user_id')
    email = data.get('email')

    if access_token and user_id:

        if not email:
            data = {'error_description' : "This VK user does not have an email"}
            return render(request, 'registration/vklogin.html', data)

        vk = vkontakte.API(token=access_token)
        profiles = vk.getProfiles(uids=str(user_id), fields='photo_100,nickname')
        profile = profiles[0]
        existing = 0
        user = 0

        try:
            # User already exists
            user = User.objects.get(email = email, vkid = user_id)
            print >>sys.stderr, "User exists"
            if user is not None:
                existing = 1
        except Exception:
            existing = 0

        if (not existing):
            try:
                m = re.match(r"(.+)\@", email)
                username = m.group(1)
                print >>sys.stderr, "Creating new user"
                print >>sys.stderr, pprint.pprint( user )

                password = str(uuid.uuid4().get_hex().upper()[0:16])
                user = User( username = username, password = password, email = email, first_name = profile['first_name'], last_name = profile['last_name'] )
                user.nickname = username
                user.vkid = user_id
                user.photourl = profile['photo_100']
                user.save()
            except Exception:
                error_description = "Cannot create new user"

        if (user and user is not None):
            login(request, user)

        return redirect('/')

    else:
        error_description = error_description or 'no data'
        data = {'error_description' : error_description}
        return render(request, 'registration/vklogin.html', data)

def vklogin(request):
    error_description = 'Cannot login via Vkontakte'
    data = {'error_description' : error_description}
    return render(request, 'registration/vklogin.html', data)

