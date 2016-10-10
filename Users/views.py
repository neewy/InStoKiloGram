from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from django.utils import timezone
from Users.models import User
from django.shortcuts import redirect
from django.contrib.auth import logout
from django.contrib.auth import authenticate, login
from django.conf import settings

import sys
import pprint

from .forms import LoginForm, RegisterForm


def index(request):
    resp = "<h1>List of latest users</h1><hr>";
    latest_users = User.objects.order_by('-pk')[:100]
    output = '<br> '.join([u.username for u in latest_users])    
    resp = resp + "<br>" + output + "<hr>"
    return HttpResponse(resp)


def accountsprofile(request):
    return redirect('/')


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
    


def vklogin(request):
    first_name = request.GET.get('first_name', False)
    last_name  = request.GET.get('last_name', False)
    photo = request.GET.get('photo', False)

    if settings.DEBUG:
        print >>sys.stderr, "Got VK data: "
        print >>sys.stderr, pprint.pprint(first_name)

    return render(request, 'registration/vklogin.html', {'first_name' : first_name, 'last_name' : last_name, 'photo' : photo})

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
