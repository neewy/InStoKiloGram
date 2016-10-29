from django import forms
from django.utils.safestring import mark_safe
from django.core.files.images import get_image_dimensions

from Users.models import User


class LoginForm(forms.Form):
    username = forms.CharField(label='Username', max_length=100)
    password = forms.CharField(label='Password', max_length=100,widget=forms.PasswordInput)

class RegisterForm(forms.Form):
    username = forms.CharField(label='Username', max_length=100)
    email = forms.EmailField(label='Email', max_length=100)
    password = forms.CharField(label='Password', max_length=100,widget=forms.PasswordInput)
    password_repeat = forms.CharField(label='Repeat Password', max_length=100, widget=forms.PasswordInput)

gender_choices = (
        ('M', 'Male'),
        ('F', 'Female'),
    )

activity_choices = (
        ('S', 'Sedentary'),
        ('LA', 'Low active'),
        ('A', 'Active'),
        ('VA', 'Very active'),
    )
goals_choices = (
        ('MWG', 'Moderate weight gain'),
        ('GWG', 'Gradual weight gain'),
        ('MCW', 'Maintain current weight'),
        ('GWL', 'Gradual weight loss'),
        ('MWL', 'Moderate weight loss'),
    )

year_choices = ('1980', '1981', '1982', '1983', '1984', '1985', '1986', '1987',
       '1988', '1989', '1990', '1991', '1992', '1993', '1994', '1995',
       '1996', '1997', '1998', '1999', '2000', '2001', '2002', '2003',
       '2004', '2005', '2006', '2007', '2008', '2009', '2010', '2011',
       '2012', '2013', '2014', '2015')
class HorizontalRadioRenderer(forms.RadioSelect.renderer):
  def render(self):
    return mark_safe(u'\n'.join([u'%s\n' % w for w in self]))



class AccountForm(forms.Form):
    class Meta:
        model = User
        fields = ('goal_weight')
    firstname = forms.CharField(label='First Name', max_length=100)
    lastname = forms.CharField(label='Last Name', max_length=100)
    gender = forms.ChoiceField(label='Gender:', widget=forms.RadioSelect(renderer=HorizontalRadioRenderer),
                               choices=gender_choices)
    start_weight = forms.FloatField(label='Current weight')
    height = forms.FloatField(label='Height')
    birth_date = forms.DateField(label='Date of birth', widget=forms.SelectDateWidget(years = year_choices,empty_label=("Choose Year", "Choose Month", "Choose Day")))
    activity_level = forms.ChoiceField(widget=forms.RadioSelect(renderer=HorizontalRadioRenderer),
                                       choices=activity_choices)
    diet_goals = forms.ChoiceField(label='Diet goals:', widget=forms.Select, choices=goals_choices)
    goal_weight = forms.FloatField(label='Weight goals')
    image = forms.ImageField(required=False)



