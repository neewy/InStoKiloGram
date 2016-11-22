from django import forms
from django.utils import timezone
from django.utils.html import conditional_escape as esc
from django.utils.safestring import mark_safe
from itertools import groupby
from calendar import HTMLCalendar, monthrange




class AddWeightForm(forms.Form):
    weight = forms.CharField(label='Weight', max_length=10)

mealtime_choices = (
        ('Breakfast', 'Breakfast'),
        ('Lunch', 'Lunch'),
        ('Dinner', 'Dinner'),
        ('Snacks', 'Snacks/Other'),
    )

year_choices = ('1980', '1981', '1982', '1983', '1984', '1985', '1986', '1987',
       '1988', '1989', '1990', '1991', '1992', '1993', '1994', '1995',
       '1996', '1997', '1998', '1999', '2000', '2001', '2002', '2003',
       '2004', '2005', '2006', '2007', '2008', '2009', '2010', '2011',
       '2012', '2013', '2014', '2015', '2016', '2017')

class AddMealForm(forms.Form):
    date = forms.DateField(label='Date', widget=forms.SelectDateWidget(years = year_choices,empty_label=("Choose Year", "Choose Month", "Choose Day")), initial=timezone.now())
    meal = forms.CharField(label='Meal', max_length=10)
    calories = forms.FloatField(label='Calories (kal)')
    mealtime = forms.ChoiceField(label='Time:', widget=forms.Select, choices=mealtime_choices)

class Meal(forms.Form):
    date = forms.DateField(label='Date', widget=forms.SelectDateWidget(years=year_choices, empty_label=(
        "Choose Year", "Choose Month", "Choose Day")), initial=timezone.now())
