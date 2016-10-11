from django import forms

class LoginForm(forms.Form):
    username = forms.CharField(label='Username', max_length=100)
    password = forms.CharField(label='Password', max_length=100,widget=forms.PasswordInput)

class RegisterForm(forms.Form):
    username = forms.CharField(label='Username', max_length=100)
    email = forms.EmailField(label='Email', max_length=100)
    password = forms.CharField(label='Password', max_length=100,widget=forms.PasswordInput)
    password_repeat = forms.CharField(label='Repeat Password', max_length=100, widget=forms.PasswordInput)
    
class AccountForm(forms.Form):
    firstname = forms.CharField(label='First Name', max_length=100)
    lastname = forms.CharField(label='Last Name', max_length=100)
    gender = forms.CharField(label='Gender', max_length = 6)
    start_weight = forms.DecimalField(label='Current weight', max_digits=3, decimal_places=2)
    height = forms.DecimalField(label='Height', max_digits=3, decimal_places=2)
    birth_date = forms.DateField(label='Date of birth')
    activity_level = forms.CharField(label='Activity level', max_length=2)
    goal_weight = forms.DecimalField(label='Weight goals', max_digits=3, decimal_places=2)
    # diet_goals = forms.CharField(label='Diet goals',max_length=100, choices=goals_choices)



