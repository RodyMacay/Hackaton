from django.shortcuts import render
from django.views.generic import DetailView
from .models import Project, Task, Category
from .filters import TaskFilter

# Vista de lista de tareas existente
def task_list(request):
    tasks = Task.objects.all()
    task_filter = TaskFilter(request.GET, queryset=tasks)
    return render(request, 'project/task_list.html', {'filter': task_filter})

# Nueva vista de resumen del proyecto
class ProjectSummaryView(DetailView):
    model = Project
    template_name = 'project/project_summary.html'
    context_object_name = 'project'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        project = self.object

        # Contar categorías relacionadas con el proyecto
        total_categories = Category.objects.filter(project=project).count()

        # Contar tareas relacionadas con el proyecto
        total_tasks = Task.objects.filter(category__project=project).count()

        # Contar tareas completadas
        completed_tasks = Task.objects.filter(category__project=project, tipo='completado').count()

        context['total_categories'] = total_categories
        context['total_tasks'] = total_tasks
        context['completed_tasks'] = completed_tasks
        return context
