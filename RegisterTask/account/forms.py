from os import name
from django.contrib.auth.models import User
from django.forms import fields
from django.forms.forms import Form
from django.forms.models import ModelForm
from django.forms.widgets import EmailInput
from account.models import Account
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate
from django.forms.fields import CharField, EmailField
from re import *
from django.core.validators import RegexValidator


class RegistrationForm(ModelForm):
	class Meta:
		model=Account
		fields=('email','name','Phone','profile_image')

		widgets = {
			'email': forms.EmailInput(attrs = {'class': 'form-control'}),
            'name': forms.TextInput(attrs = {'class': 'form-control'}),
            'Phone': forms.NumberInput(attrs = {'class': 'form-control'}),
			'profile_image':forms.ClearableFileInput(attrs={'class':'form-control'}),    
		}
	def clean(self):
		print("inside clean method")
		cleaned_data = super().clean()

		email=cleaned_data.get('email')
		name=cleaned_data.get('name')
		Phone=cleaned_data.get('Phone')
		print(email,name,Phone)

		print("inside try")
		account=Account.objects.filter(email=email).exists()
		print("account value:",account)
		if account:
			msg="Account already exists"
			self.add_error('email',msg)
		print(type(Phone))
		phone_rule='^[1-9][0-9]{9}$'
		matcher=fullmatch(phone_rule,str(Phone))
		if matcher is None:
			msg="Please enter 10 digit number"
			self.add_error('Phone',msg)
		name_rule="^[A-Za-z]{1,25}\s?[A-Za-z]{0,25}$"
		matcher1=fullmatch(name_rule,name)
		if matcher1 is None:
			msg="Please enter alphabetic characters only"
			self.add_error('name',msg)



			




			
class MyPasswordResetForm(forms.Form):
	Password = forms.CharField(widget = forms.PasswordInput(attrs = {'class': 'form-control'}))
	Confirm_Password = forms.CharField(widget = forms.PasswordInput(attrs = {'class': 'form-control'}))

	def clean(self):
		cleaned_data=super().clean()
		pass1=self.cleaned_data.get('Password')
		pass2=self.cleaned_data.get('Confirm_Password')

		print(pass1,pass2)

		if (pass1)!=(pass2):
			msg="password does not match"
			self.add_error('Password',msg)

class UserLoginForm(forms.Form):
	email=forms.CharField(widget=forms.EmailInput( attrs = {'class': 'form-control'}))
	password = forms.CharField(widget = forms.PasswordInput(attrs = {'class': 'form-control'}))

	def clean(self):
		print("isnide clean login")
		cleaned_data=super().clean()
		clean_email=cleaned_data.get("email")
		clean_password=cleaned_data.get("password")

		print(clean_email,clean_password)
		account=Account.objects.filter(email=clean_email)
		
		print("type of account:  ",type(account))
		print("account details: ",account)
		if not account:
			msg="Account does not exist, Please register"
			self.add_error('email',msg)
		else:
			user=authenticate(email=clean_email,password=clean_password)
			if not user:
				msg="Incorrect Password"
				self.add_error('password',msg)


class MyForgotPassForm(forms.Form):
	email=forms.CharField(widget=forms.EmailInput
			( attrs = {'class': 'form-control'}))

	def clean(self):
		print("inside clean forgot form")
		cleaned_data=super().clean()
		cleaned_email=cleaned_data.get("email")
		account=Account.objects.filter(email=cleaned_email).exists()
		print("account query value: ",account)
		if not account:
			msg="Email not yet registered"
			self.add_error('email',msg)







		
		
