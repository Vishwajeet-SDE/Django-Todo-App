from django.db import models

# Create your models here.

class Task(models.model):
    title = models.CharField
    description = models.TextField(blank=True)
    completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_new_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title