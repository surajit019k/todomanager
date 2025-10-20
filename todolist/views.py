from django.shortcuts import render,redirect
from django.http import HttpResponse
from todolist.models import Task
from todolist.forms import TaskForm
from django.contrib import messages
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required

# Create your views here.
def about(request):
    return render(request,"about.html",{})

def home(request):
    return render(request,"home.html",{})

@login_required
def todo(request):

    if request.method == "POST":
        form_data=TaskForm(request.POST or None)
        if form_data.is_valid():
            instance=form_data.save(commit=False)
            instance.owner=request.user
            instance.save()
            messages.success(request, "New Task Added Successfully!")
            return redirect('todo')

    all_tasks=Task.objects.filter(owner=request.user).order_by('id')
    paginator=Paginator(all_tasks,8)
    page=request.GET.get('page')

    all_tasks=paginator.get_page(page)
    context={
        'all_tasks':all_tasks,
    }
    return render(request,"todo.html",context)


@login_required
def delete_task(request,task_id):
    task_obj=Task.objects.get(id=task_id)
    if task_obj.owner == request.user:
        task_obj.delete()
        messages.success(request, f"{task_obj.task}- Deleted!")
    else:
        messages.error(request, "You are not authorized to delete this task.")
    return redirect('todo')


@login_required
def edit_task(request, task_id):
    task_obj=Task.objects.get(id=task_id)
    if request.method == "POST":
        form_data=TaskForm(request.POST or None,instance=task_obj)
        if form_data.is_valid():
            form_data.save()
            messages.success(request, "Task updated Successfully!")
            return redirect('todo')
        messages.success(request,"Error encountered in task updation!")
    else:
        context={
            'task_obj':task_obj,
        }
        return render(request, "edit.html",context)
    
@login_required
def complete_task(request, task_id):
    task_obj=Task.objects.get(id=task_id)
    if task_obj.owner == request.user:
        task_obj.is_completed=True
        task_obj.save()
        messages.success(request, f"status changed!")
    else:
        messages.error(request, "You are not authorized to complete this task.")
    return redirect('todo')


@login_required
def pending_task(request, task_id):
    task_obj=Task.objects.get(id=task_id)
    if task_obj.owner == request.user:
        task_obj.is_completed=False
        task_obj.save()
        messages.success(request, f"status changed!")
    else:
        messages.error(request, "You are not authorized to change this task.")
    return redirect('todo')

@login_required
def attendance(request):
    return render(request,"attendance.html",{})