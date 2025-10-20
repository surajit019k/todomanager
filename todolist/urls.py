
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home,name="home"),
    path('home/', views.home,name="home"),
    path('about/', views.about,name="about"),
    path('todo/', views.todo,name="todo"),
    path('todo/delete_task/<task_id>', views.delete_task,name="delete_task"),
    path('todo/edit_task/<task_id>', views.edit_task,name="edit_task"),
    path('todo/complete_task/<task_id>', views.complete_task,name="complete_task"),
    path('todo/pending_task/<task_id>', views.pending_task,name="pending_task"),
    path('attendance/', views.attendance,name="attendance"),
]