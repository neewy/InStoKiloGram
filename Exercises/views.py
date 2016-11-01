from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render, redirect, render_to_response
from django.utils import timezone

from Exercises.forms import ExerciseForm
from Exercises.models import Exercise


def exercise_list(request):
    exercises = Exercise.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'exercises/exercise_list.html', {'exercises': exercises})


def exercise_detail(request, pk):
    exercise = get_object_or_404(Exercise, pk=pk)
    return render(request, 'exercises/exercise_detail.html', {'exercise': exercise})

def exercise_new(request):
    if request.method == "POST":
        form = ExerciseForm(request.POST, request.FILES)
        if form.is_valid():
            exercise = form.save(commit=False)
            exercise.author = request.user
            exercise.published_date = timezone.now()
            exercise.image = form.cleaned_data['image']
            exercise.save()
            return redirect('exercise_detail', pk=exercise.pk)
    else:
        form = ExerciseForm()
    return render(request, 'exercises/exercise_edit.html', {'form': form})


def exercise_edit(request, pk):
    exercise = get_object_or_404(Exercise, pk=pk)
    if request.method == "POST":
        form = ExerciseForm(request.POST, request.FILES, instance=exercise)
        if form.is_valid():
            exercise = form.save(commit=False)
            exercise.author = request.user
            exercise.published_date = timezone.now()
            exercise.image = form.cleaned_data['image']
            exercise.save()
            return redirect('exercise_detail', pk=exercise.pk)
    else:
        form = ExerciseForm(instance=exercise)
    return render(request, 'exercises/exercise_edit.html', {'form': form})

def search_form(request):
    return render_to_response('exercises/search_form.html')

def search(request):
    if 'q' in request.GET and request.GET['q']:
        q = request.GET['q']
        exercises = Exercise.objects.filter(title__icontains=q).order_by('title')
        print (exercises)
        return render(request, 'exercises/search_results.html',
                      {'exercises': exercises, 'query': q})
    else:
        return render(request, 'exercises/search_results.html')

def bad_search(request):
    message = 'You searched for: %r' % request.GET['q']
    return HttpResponse(message)