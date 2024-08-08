from django.db import models
from django.utils import timezone


# Create your models here.
class Todo(models.Model):
    task = models.CharField(max_length=100, blank=False, null=False)  # Ensure this is required
    done = models.BooleanField(default=False)
    date = models.DateTimeField(default=timezone.now)  # Use timezone-aware datetime

    def __str__(self):
        return self.task

    class Meta:
        ordering = ['task']  # '-task to reverse'
