from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from patients.models import PatientProfile

class PatientRegistrationForm(UserCreationForm):
    class Meta:
        model=User
        fields=['first_name','last_name','email','username','password1','password2']


class PatientLoginForm(forms.Form):
    username=forms.CharField(max_length = 120)
    password=forms.CharField(max_length = 120)

class PatientProfileForm(ModelForm):
    class Meta:
        model=PatientProfile
        fields='__all__'



