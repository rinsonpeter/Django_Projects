from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import User
from Users.models import Order


class RegistrationForm(UserCreationForm):
    class Meta:
        model=User
        fields=['first_name','last_name','email','username','password1','password2']



class OrderForm(ModelForm):
    class Meta:
        model=Order
        fields="__all__"
