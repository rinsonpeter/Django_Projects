from django import forms
from django.contrib.auth.forms import User
from django.forms import ModelForm
from .models import Profile_model

class User_from(forms.ModelForm):

    class Meta():
        model=User
        fields=['username','email']

        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
        }

        help_texts = {
            'username': None,
        }

class Profile_form(forms.ModelForm):

    class Meta():
        model=Profile_model
        fields=['phone','profile_pic']

        widgets = {
            'phone': forms.NumberInput(attrs={'class': 'form-control'}),
            'profile_pic': forms.FileInput(attrs={'class': 'form-control'}),
        }

class Password_form(forms.Form):

    password1 = forms.CharField(max_length=120,widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(max_length=120,widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    def clean(self):
        cleaned_datas=super().clean()
        password1=cleaned_datas.get('password1')
        password2=cleaned_datas.get('password2')
        if not password1 == password2:
            msg = 'Please make sure that you enter the same password correctly in both fields'
            self.add_error('password1', msg)

class Signinform(forms.Form):
    email=forms.EmailField(max_length=120,widget=forms.EmailInput(attrs={'class': 'form-control'}))
    password = forms.CharField(max_length=120,widget=forms.PasswordInput(attrs={'class': 'form-control'}))

class Forgetpasswordform(forms.Form):
    email=forms.EmailField(max_length=200,widget=forms.EmailInput(attrs={'class': 'form-control'}))

class Edit_profileform(forms.Form):
    profile_pic=forms.ImageField(widget=forms.FileInput(attrs={'class': 'form-control'}))