

from django import forms
from apps.project.models import Task


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'tipo', 'category']
