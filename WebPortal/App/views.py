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
from .forms import SignUpForm, UserCreationForm, UserLoginForm, SlotForm, OrderRequestForm
from .models import Slot, Order


# Create your views here.
@login_required(login_url='login')
def index(request):    
    pendingOrders = Order.objects.filter(exptStatus = "completed")
    # print(p)
    return render(request, "index.html", locals())

@login_required(login_url='login')
def acceptRequest(request , pk):
    order = get_object_or_404(Order, id=pk)
    if request.method == "POST":
        order.exptStatus = "paid"
        order.save()
    return redirect("/")
        
@login_required(login_url='login')
def declineRequest(request , pk):
    order = get_object_or_404(Order, id=pk)
    if request.method == "POST":
        order.exptStatus = "rejected"
        order.save()
    return redirect("/")


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
    activeSlots = []
    slots = Slot.objects.filter(numberOfSeats__gt = 0)
    slots = slots.filter(exptDate__gte = datetime.date.today())
    orders = Order.objects.filter(candidate = request.user)
    if slots:
        print("OK YES !")
    for slot in slots:
        if orders.filter(slot = slot):
            activeSlots.append(slot)
    # print("Print", activeSlots, list(slots))
    return render(request, "viewSlots.html", locals())

@login_required(login_url='login')
def bookSlot(request, pk):
    slot =  get_object_or_404(Slot, id=pk)
    user = request.user
    if request.method == "POST":
        orderReq = OrderRequestForm(request.POST)
        if slot.numberOfSeats > 0:
            if orderReq.is_valid():
                req = orderReq.save(commit = False)
                req.candidate = user
                req.dateBooked = datetime.date.today()
                req.isBooked = False
                req.slot = slot
                slot.numberOfSeats -= 1
                slot.save()
                req.save()
                print("OK Saved!")
                return redirect('/viewSlots')
            else:
                for field in orderReq:
                    print("Field Error:", field.name,  field.errors)
                print("OK Not Saved!")
        else:
            return HttpResponse("Cannot Book! Seats Filled.")
    print("OK Not Saved!2")
    return redirect("/viewSlots")


@login_required(login_url='login')
def unbookSlot(request, pk):
    slot =  get_object_or_404(Slot, id=pk)
    user = request.user
    orders = Order.objects.filter(candidate = user, slot = slot)
    if request.method == "POST":
        for order in orders:
            order.delete()
        slot.numberOfSeats += 1
        slot.save()
    return redirect("/viewSlots")

@login_required(login_url='login')
def mySlots(request):
    orders = Order.objects.filter(candidate = request.user)
    upcomingSlots = []
    pastOrders = []

    for order in orders:
        if order.slot.exptDate < datetime.date.today():
            pastOrders.append(order)
        else:
            upcomingSlots.append(order.slot)
    
    return render(request, "mySlots.html", locals())

@login_required(login_url='login')
def requestCompletion(request, pk):
    if request.method == "POST":
        order = get_object_or_404(Order, id=pk)
        order.exptStatus = 'completed'
        order.save()
    return redirect("/mySlots")


# @login_required(login_url='login')
# def completeRequest(request, pk):
#     order = get_object_or_404(Order, id=pk)
#     if request.method == "POST":

