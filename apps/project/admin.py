from django.contrib import admin
from apps.project.models import Category, Project, Task

# Register your models here.
admin.site.register(Project)
admin.site.register(Task)
admin.site.register(Category)
