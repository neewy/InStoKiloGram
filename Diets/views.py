from django.shortcuts import render, redirect
from django.utils import timezone

from Diets.forms import DietForm, DietReviewForm
from Diets.models import Diet, DietReview
from django.shortcuts import render, get_object_or_404


def diet_list(request):
    diets = Diet.objects.filter().order_by('published_date')
    reviews = sorted(DietReview.objects.all(), cmp=DietReview.sort_reviews_avg, reverse=True)
    return render(request, 'diet/diet_list.html', {
        'two_main_diets': diets[:2],
        'other_diets': diets[2:],
        'reviews': reviews
    })


def diet_detail(request, pk):
    diet = get_object_or_404(Diet, pk=pk)
    return render(request, 'diet/diet_detail.html', {'diet': diet})


def new_diet(request):
    if request.method == "POST":
        form = DietForm(request.POST, request.FILES)
        if request.user.has_perm('diet.add_diet'):
            if form.is_valid():
                diet = form.save(commit=False)
                diet.author = request.user
                diet.text = request.POST['text']
                diet.name = request.POST['name']
                diet.published_date = timezone.now()
                diet.image = form.cleaned_data['image']
                diet.save()
                for recipe in request.POST.get('recipes', False):
                    diet.recipes.add(recipe)
                return redirect('diet_detail', pk=diet.pk)
    else:
        form = DietForm()
    return render(request, 'diet/new_diet.html', {'form': form})


def diet_edit(request, pk):
    diet = get_object_or_404(Diet, pk=pk)
    if request.method == "POST":
        form = DietForm(request.POST, request.FILES, instance=diet)
        if form.is_valid():
            diet = form.save(commit=False)
            diet.author = request.user
            diet.text = request.POST['text']
            diet.name = request.POST['name']
            diet.published_date = timezone.now()
            diet.image = form.cleaned_data['image']
            diet.save()
            #fixme: ONLY THE LAST ONE IS ADDED
            for recipe in request.POST.get('recipes', False):
                diet.recipes.add(recipe)
            return redirect('diet_detail', pk=diet.pk)
    else:
        form = DietForm(instance=diet)
    return render(request, 'diet/new_diet.html', {'form': form})


def new_review(request):
    if request.method == "POST":
        form = DietReviewForm(request.POST, request.FILES)
        if form.is_valid():
            review = form.save(commit=False)
            review.author = request.user
            review.pub_date = timezone.now()
            review.title = request.POST['title']
            review.rating = request.POST['rating']
            review.review_text = request.POST['review_text']
            review.save()
            return redirect('diet_list')
    else:
        form = DietReviewForm()
    return render(request, 'diet/new_review.html', {'form': form})


def review_edit(request, pk):
    review = get_object_or_404(DietReview, pk=pk)
    if request.method == "POST":
        form = DietReviewForm(request.POST, request.FILES, instance=diet)
        if form.is_valid():
            review = form.save(commit=False)
            review.author = request.user
            review.pub_date = timezone.now()
            review.title = request.POST['title']
            review.rating = request.POST['rating']
            review.review_text = request.POST['review_text']
            review.save()
            return redirect('diet_list', pk=review.pk)
    else:
        form = DietReviewForm(instance=review)
    return render(request, 'diet/new_review.html', {'form': form})
