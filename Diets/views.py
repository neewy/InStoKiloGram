from django.shortcuts import render

from Diets.models import Diet, DietReview


def diet_list(request):
    diets = Diet.objects.filter().order_by('published_date')
    reviews = sorted(DietReview.objects.all(), cmp=DietReview.sort_reviews_avg, reverse=True)
    return render(request, 'diet/diet_list.html', {
        'two_main_diets': diets[:2],
        'other_diets': diets[2:],
        'reviews': reviews
    })