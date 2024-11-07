from django.db import models

from apps.core.models import ModelBase
from apps.security.models import User

# Create your models here.

class Project(ModelBase):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=100, default="Nombre por defecto")
    description = models.TextField(null=True, blank=True)

    class Meta:
        verbose_name = "Project"
        verbose_name_plural = "Projects"
        ordering = ['name']

    def __str__(self):
        return self.name

        return self.name


class Category(ModelBase):
    name = models.CharField(max_length=100)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"
        ordering = ['name']  # Ordenar por nombre de categoría

    def __str__(self):
        return self.name

class Task(ModelBase):
    COMPLETION_STATUS = [
        ('completado', 'Completado'),
        ('pendiente', 'Pendiente'),
    ]
    
    title = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    tipo = models.CharField(max_length=10, choices=COMPLETION_STATUS, null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Task"
        verbose_name_plural = "Tasks"
        ordering = ['title']  # Ordenar por título de la tarea

    def __str__(self):
        return self.title
