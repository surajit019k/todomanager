from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from django.contrib import messages
from .forms import CustomRegistrationForm

def register(request):
    if request.method == "POST":
        register_form=CustomRegistrationForm(request.POST)
        if register_form.is_valid():
            register_form.save()
            messages.success(request, "User Created Successfully")
            return redirect('todo')
    else:
        register_form=CustomRegistrationForm()
    return render(request,"register.html",{'register_form':register_form})