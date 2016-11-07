from django.db.models import DateField
from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from django.utils import timezone
from Users.models import User
from Weight.models import Weight
from django.shortcuts import redirect
from django.contrib.auth import logout
from django.contrib.auth import authenticate, login
from django.conf import settings

import pprint
import datetime

import string
import random
import uuid
import sys

from .forms import AddWeightForm

def wadd(request):
    form = AddWeightForm()
    now = datetime.datetime.now()
    
    if request.method == 'POST':
        try:
            the_weight = int(request.POST.get('weight', False))
        except:
            return render(request, 'add.html', {'form' : form, 'now': now.strftime("%Y-%m-%d %H:%M:%S"), 'invalid':1 })
        
        w = Weight(date=now, user_id=request.user.id, weight=the_weight )
        w.save()
        return redirect('/weight/')
    
    return render(request, 'add.html', {'form' : form, 'now': now.strftime("%Y-%m-%d %H:%M:%S")})

def wview(request):
   
    whistory = Weight.objects.filter(user_id=request.user.id).order_by('-id')[:100]
    
#    output = '<br> '.join([str(w.date) + str(w.weight) for w in whistory])

    wds = []
    
    for w in whistory:
        wds.extend([{'date':w.date.strftime("%Y-%m-%d %H:%M:%S"),'weight':str(w.weight), 'dateraw':w.id}])
    
    return render(request, 'weight_view.html', {'wds': wds})
    

def wdelete(request):
    if request.method == 'POST':
        try:
            id = int(request.POST.get('id', False))
            user_id=request.user.id
            Weight.objects.filter(id=id,user_id=user_id).delete()
        except:
            1
            
    return redirect('/weight/')

def wstat(request):
    whistory = Weight.objects.filter(user_id=request.user.id).order_by('-id')[:100]
    
    wds = []
    
    for w in whistory:
        wds.extend([{'date':w.date.strftime("%Y-%m-%d %H:%M:%S"),'weight':str(w.weight), 'dateraw':w.id}])
    
    return render(request, 'view.html', {'wds': wds, 'stat':1})
    



