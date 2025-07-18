from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Task(models.Model):
    priority_choices = [('Low', 'Low'), ('Medium', 'Medium'), ('High', 'High')]


    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=250)
    description = models.TextField(blank=True)
    priority = models.CharField(max_length=20, choices=priority_choices, default='Medium')
    due_date = models.DateField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


