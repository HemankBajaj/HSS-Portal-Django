from django.db import models
from django.urls import reverse   # ---> add
from django.contrib.auth.models import User

# Create your models here.

class Slot(models.Model):
    exptTitle = models.CharField(max_length = 50)
    exptDesc = models.CharField(max_length = 100)
    exptDate = models.DateField()
    numberOfSeats = models.IntegerField()

    startTime = models.TimeField()
    endTime = models.TimeField()

    candidateList = models.ManyToManyField(
        User, 
        through="Order",
        through_fields=("slot", "candidate"), 
    )


class Order(models.Model):
    status_choice= [
        ('pending', 'Pending'),
        ('completed', 'Completed'),
        ('paid ', 'Paid '),
    ]

    candidate = models.ForeignKey(User, on_delete=models.CASCADE)
    slot = models.ForeignKey(Slot, on_delete=models.CASCADE)
    dateBooked = models.DateField(auto_now_add=True)
    exptStatus = models.CharField(max_length=30,choices=status_choice,default='pending')
    

