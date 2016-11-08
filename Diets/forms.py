from django import forms
from .models import Diet, DietReview


class DietForm(forms.ModelForm):
    class Meta:
        model = Diet
        fields = ('name', 'text', 'image', 'recipes')


class DietReviewForm(forms.ModelForm):
    class Meta:
        model = DietReview
        fields = ('title', 'diet', 'rating', 'review_text')
