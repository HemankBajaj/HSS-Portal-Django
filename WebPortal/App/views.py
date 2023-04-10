from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth import authenticate
import datetime
# from django.contrib.auth.models import User, auth
from django.contrib.auth import login,logout
# from django.contrib import messages #import messages
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.db import models
from django.contrib.auth.decorators import login_required,user_passes_test
# from . import forms,models
from .forms import SignUpForm, UserCreationForm, UserLoginForm, SlotForm
from .models import Slot, Order


# Create your views here.
@login_required(login_url='login')
def index(request):
    # slots=models.Slot.objects.filter(numberOfSeats > 0)
    # slots = slots.filter(exptDate > datetime.date.today())

    context = {
        # "slots" : slots, 
    }
    
    return render(request, "index.html", context)

# def bookSlot(request, pk):


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

@login_required(login_url='login')
def logoutUser(request):
    logout(request)
    return redirect("/")

@login_required(login_url='login')
def addSlot(request):
    form = SlotForm()
    if request.method == "POST":
        form = SlotForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/viewSlots")
    return render(request, 'addSlot.html', {"form" : form})


@login_required(login_url='login')
def deleteSlot(request, pk):
    slot = get_object_or_404(Slot, id=pk)
    orders=Order.objects.filter(slot=slot)
    if request.method == "POST":
        slot.delete()
        for order in orders:
            order.delete()
        return redirect('/viewSlots')
@login_required(login_url='login')
def updateSlot(request, pk):
    slot =  get_object_or_404(Slot, id=pk)
    form = SlotForm(instance = slot)
    if request.method == "POST":
        print("Update Request")
        form = SlotForm(request.POST,instance=slot)
        if form.is_valid():
            slot1 = form.save(commit=False)
            slot1.save()
            return redirect("/viewSlots")
    return render(request, "updateSlot.html", locals())


@login_required(login_url='login')
def viewAvailableSlots(request):
    slots=Slot.objects.filter(numberOfSeats__gt = 0)
    slots = slots.filter(exptDate__gte = datetime.date.today())
    context = {
        "slots" : slots, 
    }
    return render(request, "viewSlots.html", context)


## Booking of Slot, Slot Information, Edit Slot
@login_required(login_url='login')
def viewSlot(request, pk):
    slot =  get_object_or_404(Slot, id=pk)
    orders = Order.objects.filter(slot = slot)
    form = SlotForm(instance = slot)
    if request.method == "POST":
        if "update" in request.POST: ## Update a Slot
            print("Update Request")
            form = SlotForm(request.POST,instance=slot)
            if form.is_valid():
                slot1 = form.save(commit=False)
                slot1.save()
                return redirect("/viewSlots")
        elif "delete_slot" in request.POST:
            print("Delete Request!")
            slot.delete()
            for order in orders:
                order.delete()
            redirect('/')
        else:  ## Logic For Booking a Slot
            pass

    return render(request, 'slotDetails.html', locals())








