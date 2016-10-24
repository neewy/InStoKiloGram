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
    
    resp = "<h1>List of latest users</h1><hr>";
    whistory = Weight.objects.order_by('-date')[:100]
    
    output = '<br> '.join([str(w.date) + str(w.weight) for w in whistory])

    wds = []
    
    for w in whistory:
        wds.extend([{'date':w.date.strftime("%Y-%m-%d %H:%M:%S"),'weight':str(w.weight)}])
    
    return render(request, 'view.html', {'wds': wds})
    
