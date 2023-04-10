from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User



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

    
