from django import forms

class AddWeightForm(forms.Form):
    weight = forms.CharField(label='Weight', max_length=10)
