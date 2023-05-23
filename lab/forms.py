from django import forms
from lab.models import *
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class contectform(forms.ModelForm):
    class Meta:
        fields='__all__'
        model=contect

class signupform(UserCreationForm):
    class Meta:
        fields=('first_name','last_name','username','email','password1','password2')
        model=User

class appointmentform(forms.ModelForm):
    class Meta:
        fields='__all__'
        model=Appointment

class Subcribeform(forms.ModelForm):
    class Meta:
        fields='__all__'
        model=Subcribe       

