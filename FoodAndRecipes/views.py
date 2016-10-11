from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render, redirect, render_to_response
from django.utils import timezone

from FoodAndRecipes.forms import RecipeForm
from FoodAndRecipes.models import Recipe


def recipe_list(request):
    recipes = Recipe.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'foodandrecipes/recipe_list.html', {'recipes': recipes})


def recipe_detail(request, pk):
    recipe = get_object_or_404(Recipe, pk=pk)
    return render(request, 'foodandrecipes/recipe_detail.html', {'recipe': recipe})

def recipe_new(request):
    if request.method == "POST":
        form = RecipeForm(request.POST, request.FILES)
        if form.is_valid():
            recipe = form.save(commit=False)
            recipe.author = request.user
            recipe.published_date = timezone.now()
            recipe.image = form.cleaned_data['image']
            recipe.save()
            return redirect('recipe_detail', pk=recipe.pk)
    else:
        form = RecipeForm()
    return render(request, 'foodandrecipes/recipe_edit.html', {'form': form})


def recipe_edit(request, pk):
    recipe = get_object_or_404(Recipe, pk=pk)
    if request.method == "POST":
        form = RecipeForm(request.POST, request.FILES, instance=recipe)
        if form.is_valid():
            recipe = form.save(commit=False)
            recipe.author = request.user
            recipe.published_date = timezone.now()
            recipe.image = form.cleaned_data['image']
            recipe.save()
            return redirect('recipe_detail', pk=recipe.pk)
    else:
        form = RecipeForm(instance=recipe)
    return render(request, 'foodandrecipes/recipe_edit.html', {'form': form})

def search_form(request):
    return render_to_response('foodandrecipes/search_form.html')

def search(request):
    if 'q' in request.GET and request.GET['q']:
        q = request.GET['q']
        recipes = Recipe.objects.filter(title__icontains=q).order_by('title')
        print (recipes)
        return render(request, 'foodandrecipes/search_results.html',
            {'recipes': recipes, 'query': q})
    else:
        return render(request, 'foodandrecipes/search_results.html')

def bad_search(request):
    message = 'You searched for: %r' % request.GET['q']
    return HttpResponse(message)