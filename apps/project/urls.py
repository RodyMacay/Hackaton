from django.urls import path
from . import views
from .views import ProjectSummaryView

app_name = 'project'

urlpatterns = [
    path('tasks/', views.task_list, name='task_list'),
    path('project/<int:pk>/summary/', ProjectSummaryView.as_view(), name='project_summary'),
    # otras rutas...
]
