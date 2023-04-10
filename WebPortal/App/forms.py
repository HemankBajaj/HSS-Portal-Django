from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from .models import Slot, Order



class SignUpForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["username"].widget.attrs.update({
            "required" : "", 
            "type":"text", 
            "class":"form-control" ,
            "id":"inputName",
            "placeholder":"Enter your name"
        })
        self.fields["email"].widget.attrs.update({
            "required" : "", 
            "type":"email", 
            "class":"form-control" ,
            "id":"inputEmail",
            "placeholder":"Enter your Email"
        })
        self.fields["password1"].widget.attrs.update({
            "required" : "", 
            "type":"password", 
            "class":"form-control" ,
            "id":"inputPassword",
            "placeholder":"Password"
        })
        self.fields["password2"].widget.attrs.update({
            "required" : "", 
            "type":"password", 
            "class":"form-control" ,
            "id":"inputConfirmPassword",
            "placeholder":"Confirm Password"
        })

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]
        
class UserLoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["username"].widget.attrs.update({
            "required" : "", 
            "type":"text", 
            "class":"form-control" ,
            "id":"inputName",
            "placeholder":"Username"
        })
        self.fields["password"].widget.attrs.update({
            "required" : "", 
            "type":"password", 
            "class":"form-control" ,
            "id":"inputPassword",
            "placeholder":"Password"
        })
    class Meta:
        model = User
        fields = ["username", "password"]

    
class SlotForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["exptTitle"].widget.attrs.update({
            "required" : "", 
            "type":"text", 
            "class":"form-control" ,
            "id":"exptTitle",
            "placeholder":"Enter Experiment Title"
        })
        self.fields["exptDesc"].widget.attrs.update({
            "required" : "", 
            "type":"text", 
            "class":"form-control" ,
            "id":"exptDesc",
            "placeholder":"Enter Experiment Description"
        })
        self.fields["exptDate"].widget.attrs.update({
            "required" : "", 
            "type":"date", 
            "class":"form-control" ,
            "id":"exptDate",
            "placeholder":"Enter Date"
        })
        self.fields["startTime"].widget.attrs.update({
            "required" : "", 
            "type":"time", 
            "class":"form-control" ,
            "id":"startTime",
            "placeholder":"Enter start time", 
        })
        self.fields["endTime"].widget.attrs.update({
            "required" : "", 
            "type":"time", 
            "class":"form-control" ,
            "id":"endTime",
            "placeholder":"Enter end time"
        })
        self.fields["numberOfSeats"].widget.attrs.update({
            "required" : "", 
            "type":"number", 
            "class":"form-control" ,
            "id":"numberOfSeats",
            "placeholder":"Enter number of seats"
        })

    class Meta:
        model = Slot
        exclude=['candidateList']


class OrderRequestForm(forms.ModelForm):
    class Meta:
        model = Order
        exclude = ['candidate', 'slot', 'dateBooked', 'exptStatus', 'isBooked']