from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth import authenticate


# from django.contrib.auth.models import User, auth
from django.contrib.auth import login,logout
# from django.contrib import messages #import messages
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
# from django.db import models
from django.contrib.auth.decorators import login_required,user_passes_test
# from . import forms,models
from .forms import SignUpForm, UserCreationForm, UserLoginForm

# Create your views here.
@login_required(login_url='login')
def index(request):
    return render(request, "index.html")

def signUp(request):
    form = SignUpForm()
    context = {"form": form}
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/login')
        for field in form:
            print("Field Error:", field.name,  field.errors)

        print("Form Not Valid")
    return render(request,"signup.html", context)       


def loginUser(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            new_user = authenticate(username=username, password=password)
            if new_user is not None:
                login(request, new_user)
                return redirect("/")
            for field in form:
                print("Field Error:", field.name,  field.errors)
            return redirect('/')
    else:
        form = UserLoginForm()
    return render(request, 'login.html', {'form': form})

def logoutUser(request):
    logout(request)
    return redirect("/")


