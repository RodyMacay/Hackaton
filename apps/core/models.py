from django.db import models

# Create your models here.


class ModelBase(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    created_by = models.CharField(max_length=100, blank=True, null=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, blank=True, null=True)
    update_by = models.CharField(max_length=100, blank=True, null=True, editable=False)

    class Meta:
        abstract = True
