"""EmployeeManagement URL Configuration

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
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from Employee.views import viewcreateDept,viewDeleteDept, viewUpdateDept, viewCreateEmp, viewDeleteEmp, viewUpdateEmp


urlpatterns = [

    path('',viewcreateDept,name='viewCreateDept'),
    path("delete/<int:pk>", viewDeleteDept, name = 'viewDeleteDept'),
    path("update/<int:pk>", viewUpdateDept, name = 'viewUpdateDept'),
    path("employee/", viewCreateEmp, name = 'viewCreateEmp'),
    path("deleteEmp/<int:pk>", viewDeleteEmp, name = 'viewDeleteEmp'),
    path("updateEmp/<int:pk>", viewUpdateEmp, name = 'viewUpdateEmp'),
    
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
