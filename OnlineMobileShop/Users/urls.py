
from django.contrib import admin
from django.urls import path
from Users.views import registraion, signIn

urlpatterns = [
    path('register',registraion,name='register'),
    path('signin',signIn,name='signin'),


]
