from django.shortcuts import render, redirect, get_object_or_404
from .models import Task


def task_list(request):
    tasks = Task.objects.all()
    #SELECT * FROM myToDo2_task ORDER BY completed, due_date, created_at
    #tasks = Task.objects.raw('SeLECT * FROM myToDo2_task ORDER BY completed, due_date, created_at')
    return render(request, 'myToDo2/task_list.html', {'tasks': tasks})

def task_create(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        due_date = request.POST.get('due_date')
        # ORM
        Task.objects.create(title=title, due_date=due_date)
        # Raw SQL
        # from django.db import connection
        # with connection.cursor() as cursor:
        #     cursor.execute('INSERT INTO myToDo2_task (title, due_date) VALUES 
        return redirect('task_list')
    return render(request, 'myToDo2/task_form.html')

def task_delete(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == 'POST':
        task.delete()
        # Raw SQL
        # from django.db import connection
        # with connection.cursor() as cursor:
        #     cursor.execute('DELETE FROM myToDo2_task WHERE id = %s', [pk])    
        return redirect('task_list')
    return render(request, 'myToDo2/task_list.html', {'task': task})