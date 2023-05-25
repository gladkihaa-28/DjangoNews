from django.shortcuts import render, redirect
from .models import Task
from .forms import TaskForm
from .parser import get_news


def index(request):
    tasks = get_news()
    return render(request, 'main/index.html', {'title': 'Главная новостная страница', 'tasks': tasks})


def forum(request):
    tasks = Task.objects.all()
    return render(request, 'main/forum.html', {'title': 'Новостной форум', 'tasks': tasks})


def create(request):
    error = ''
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("forum")
        else:
            error = 'Форма не корректна!'

    form = TaskForm()
    context = {
        'form': form,
        'error': error
    }
    return render(request, 'main/create.html', context)


