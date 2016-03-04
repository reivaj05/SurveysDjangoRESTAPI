from __future__ import unicode_literals

from django.db import models


# Create your models here.
class Survey(models.Model):

    class Meta:
        verbose_name = "Survey"
        verbose_name_plural = "Surveys"

    title = models.CharField(max_length=80)
    description = models.TextField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.title
