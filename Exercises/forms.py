from django import forms

from Exercises.models import Exercise


class ExerciseForm(forms.ModelForm):
    class Meta:
        model = Exercise
        fields = ('title', 'text', 'image')