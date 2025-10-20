from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Task(models.Model):
    owner=models.ForeignKey(User, on_delete=models.CASCADE,default=None)
    task=models.CharField(max_length=100)
    is_completed=models.BooleanField(default=False)

    def __str__(self):
        return f"{self.task}"
    
class Student(models.Model):
    name=models.CharField(max_length=100)

    def __str__(self):
        return f"{self.name}"