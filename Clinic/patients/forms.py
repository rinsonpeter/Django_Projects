from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from patients.models import *


class PatientRegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'username', 'password1', 'password2']


class PatientLoginForm(forms.Form):
    username = forms.CharField(max_length = 120)
    password = forms.CharField(max_length = 120)
    widgets = {
        'username': forms.TextInput(attrs = {'class': 'form-control'}),
        'password': forms.PasswordInput(attrs = {'class': 'form-control'}),

    }


class PatientProfileForm(ModelForm):
    class Meta:
        model = PatientProfile
        fields = '__all__'
        widgets = {

            'user': forms.TextInput(attrs = {'class': 'form-control','readonly':'readonly'}),
            'phonenumber': forms.TextInput(attrs = {'class': 'form-control'}),
            'bloodgroup': forms.TextInput(attrs = {'class': 'form-control'}),
            'age': forms.NumberInput(attrs = {'class': 'form-control'}),
            'address': forms.TextInput(attrs = {'class': 'form-control'}),

        }

class BookingForm(ModelForm):
    class Meta:
        model=Booking
        readonly = ["user"]
        fields=['doctor','user','date']
        widgets = {

            'user': forms.TextInput(attrs = {'class': 'form-control', 'readonly': 'readonly'}),
            'doctor': forms.TextInput(attrs = {'class': 'form-control'}),
            'date': forms.SelectDateWidget(attrs = {'class': 'form-control'}),

        }


