from django.forms import ModelForm
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from Trainer.models import *


class TrainerRegForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email',
                  'username', 'password1', 'password2']


class TrainerLoginForm(forms.Form):
    username = forms.CharField(max_length=120)
    password = forms.CharField(max_length=120)


class TrainerCreationForm(ModelForm):
    class Meta:
        model = TrainerProfile
        fields = '__all__'
        widgets = {

            'user': forms.TextInput(attrs={'class': 'form-control', 'readonly': 'readonly'}),
            'skill': forms.Select(attrs={'class': 'form-control'}),
            'Age': forms.NumberInput(attrs={'class': 'form-control'}),
            'experience': forms.TextInput(attrs={'class': 'form-control'}),

        }
class ApplicationForm(ModelForm):
    class Meta:
        model=Applications
        fields='__all__'
        widgets={
            'user': forms.TextInput(attrs={'class': 'form-control', 'readonly': 'readonly'}),
            'skill': forms.TextInput(attrs={'class': 'form-control'}),
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'experience': forms.TextInput(attrs={'class': 'form-control'}),
            'Address':forms.Textarea(attrs={'class': 'form-control'}),
            'status': forms.HiddenInput(),



        }
