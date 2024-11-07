from django.urls import path
from . import views

app_name = 'project'

urlpatterns = [
    path('tasks/', views.task_list, name='task_list'),
    # otras rutas...
]