from django.shortcuts import render

from django.utils import timezone
from Weight.models import Weight, FoodDiary
from django.shortcuts import redirect
import datetime

import sys

from .forms import AddWeightForm, AddMealForm


def wadd(request):
    form = AddWeightForm()
    now = datetime.datetime.now()

    if request.method == 'POST':
        try:
            the_weight = int(request.POST.get('weight', False))
        except:
            return render(request, 'add.html', {'form': form, 'now': now.strftime("%Y-%m-%d %H:%M:%S"), 'invalid': 1})

        w = Weight(date=now, user_id=request.user.id, weight=the_weight)
        w.save()
        return redirect('/weight/')

    return render(request, 'add.html', {'form': form, 'now': now.strftime("%Y-%m-%d %H:%M:%S")})


def wview(request):
    whistory = Weight.objects.filter(user_id=request.user.id).order_by('-id')[:100]

    #    output = '<br> '.join([str(w.date) + str(w.weight) for w in whistory])

    wds = []

    for w in whistory:
        wds.extend([{'date': w.date.strftime("%Y-%m-%d %H:%M:%S"), 'weight': str(w.weight), 'dateraw': w.id}])

    return render(request, 'view.html', {'wds': wds})


def wdelete(request):
    if request.method == 'POST':
        try:
            id = int(request.POST.get('id', False))
            user_id = request.user.id
            Weight.objects.filter(id=id, user_id=user_id).delete()
        except:
            1

    return redirect('/weight/')


def wstat(request):
    whistory = Weight.objects.filter(user_id=request.user.id).order_by('-id')[:100]

    wds = []

    for w in whistory:
        wds.extend([{'date': w.date.strftime("%Y-%m-%d %H:%M:%S"), 'weight': str(w.weight), 'dateraw': w.id}])

    return render(request, 'view.html', {'wds': wds, 'stat': 1})


def mealstat(request):
    mealhistory = FoodDiary.objects.filter(user_id=request.user.id, date=timezone.now()).order_by('-id')[:100]

    mds = []

    for meal in mealhistory:
        mds.extend([{'meal': meal.food, 'date': meal.date.strftime("%Y-%m-%d %H:%M:%S"), 'calories': meal.calories,
                     'dateraw': meal.id, 'mealtime': meal.mealtime}])

    return render(request, 'view_meal.html', {'mds': mds, 'stat': 1})


def mealadd(request):

    now = datetime.datetime.now()

    if request.method == 'POST':
        form = AddMealForm(request.POST, request.FILES)
        for error in form.errors:
            print>> sys.stderr, error
        if form.is_valid():
            date = form.cleaned_data.get('date', False)
            meal = request.POST.get('meal', False)
            calories = request.POST.get('calories', False)
            mealtime = request.POST.get('mealtime', False)
            try:
                food = FoodDiary(date=date, user_id=request.user.id, food=meal, calories=calories, mealtime=mealtime)
                food.save()
                return redirect('/accounts/profile/fooddiary/')

            except:
                return render(request, 'add_meal.html',
                              {'form': form, 'now': now.strftime("%Y-%m-%d %H:%M:%S"), 'invalid': 1})


    form = AddMealForm()

    return render(request, 'add_meal.html', {'form': form, 'now': now.strftime("%Y-%m-%d %H:%M:%S")})
