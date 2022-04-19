from django.shortcuts import render, redirect
from .models import *
from .forms import *

# Create your views here.

def index(request):
    tasks = Tasks.objects.all()

    form = TaskForm()

    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect("/")
     
    return render(request, 'list.html', {'tasks':tasks, 'form':form})


def updateTask(request, pk):
    task = Tasks.objects.get(id=pk)
    form = TaskForm(instance=task)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect("/")

    return render(request, 'update_task.html', {'form':form})


def deleteTask(request, pk):
    item = Tasks.objects.get(id=pk)
    if request.method == 'POST':
        item.delete()
        return redirect("/")
    return render(request, 'delete.html', {'item':item})