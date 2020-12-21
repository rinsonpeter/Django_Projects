from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms    
from books.models import Book


class BookCreateForm(ModelForm):
    class Meta:
        model=Book
        fields='__all__'
    
    def clean(self):
        print("Cleaning")
        

class UserRegistrationForm(UserCreationForm):
    class Meta:
        model=User
        fields=['first_name','last_name','email','username','password1','password2']

class LoginForm(forms.Form):
    username=forms.CharField(max_length=120)
    password=forms.CharField(max_length=30,widget=forms.PasswordInput)
    


1`1