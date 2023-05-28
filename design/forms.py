from django.forms import ModelForm
from .models import Customer,Booking,Avis
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class createUserForm(UserCreationForm):
  class Meta:
    model=User
    fields=['username','email','password1','password2']

class CustomerForm(ModelForm):
  class Meta:
    model=Customer
    fields='__all__'
    exclude=['user'] #pour filtrer

class BookingForm(ModelForm):
  class Meta:
    model=Booking
    fields='__all__'

class AvisForm(ModelForm):
  class Meta:
    model=Avis
    fields='__all__'