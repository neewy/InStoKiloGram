from django.shortcuts import get_object_or_404, render, redirect, render_to_response

from Food.forms import FoodForm
from Food.models import Food


def food_list(request):
    food = Food.objects.order_by('name')
    return render(request, 'food/food_list.html', {'food': food})


def food_detail(request, pk):
    food = get_object_or_404(Food, pk=pk)
    return render(request, 'food/food_detail.html', {'food': food})

def food_new(request):
    if request.method == "POST":
        form = FoodForm(request.POST, request.FILES)
        if form.is_valid():
            food = form.save(commit=False)
            food.name = request.user
            food.save()
            return redirect('food_detail', pk=food.pk)
    else:
        form = FoodForm()
    return render(request, 'food/food_edit.html', {'form': form})


def food_edit(request, pk):
    food = get_object_or_404(Food, pk=pk)
    if request.method == "POST":
        form = FoodForm(request.POST, request.FILES, instance=food)
        if form.is_valid():
            food = form.save(commit=False)
            food.name = request.user
            food.save()
            return redirect('food_detail', pk=food.pk)
    else:
        form = FoodForm(instance=food)
    return render(request, 'food/food_edit.html', {'form': form})