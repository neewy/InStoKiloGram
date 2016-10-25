from django import forms

from Food.models import Food


class FoodForm(forms.ModelForm):
    class Meta:
        model = Food
        fields = ('name', 'description', 'calories')