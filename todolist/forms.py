from django import forms
from todolist.models import Task, Student

class TaskForm(forms.ModelForm):
    class Meta:
        model=Task
        fields=['task','is_completed']

class StudentForm(forms.ModelForm):
    class Meta:
        model=Student
        fields=['name']