"""RegisterTask URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.contrib.auth import logout
from django.urls import path, include
from account import views
from django.conf.urls import url

urlpatterns = [
    path('home/',views.home,name='home'),
    path('logoutview',views.logoutview,name='logoutview'),
    path('reset_pass/',views.reset_pass,name='reset_pass'),
    path('register/',views.register_view,name='register'),
    path('reg_confirm/',views.reg_confirm,name='reg_confirm'),
    path('user_login',views.user_login,name='user_login'),
    path('activate/<slug:uidb64>/<slug:token>/', views.activate, name='activate'),
  
]
