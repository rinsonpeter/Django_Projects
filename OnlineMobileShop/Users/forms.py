from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import User
from Users.models import Order
from django import forms


class RegistrationForm(UserCreationForm):
    class Meta:
        model=User
        fields=['first_name','last_name','email','username','password1','password2']



class OrderForm(ModelForm):
    class Meta:
        model=Order
        fields="__all__"
        widgets = {
            'mobile': forms.TextInput(attrs = {'class': 'form-control','readonly':'readonly'}),
            'user': forms.TextInput(attrs = {'class': 'form-control','readonly':'readonly'}),
             'quantity': forms.NumberInput(attrs = {'class': 'form-control'}),
             'address': forms.Textarea(attrs = {'class': 'form-control'}),
             'status': forms.HiddenInput(),
            }