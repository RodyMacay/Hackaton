from django.shortcuts import render
from .models import Task
from .filters import TaskFilter

def task_list(request):
    tasks = Task.objects.all()
    task_filter = TaskFilter(request.GET, queryset=tasks)
    return render(request, 'project/task_list.html', {'filter': task_filter})