



from django.contrib import admin
from django.urls import path
from Trainer.views import *

urlpatterns = [
    path('',trainerLogin,name='trainerLogin'),
    path('trainerReg',trainerReg,name='trainerReg'),
    path('trainerHome',trainerHome,name='trainerHome'),
    path('trainerProfile',createTrainerProfile,name='createTrainerProfile'),
    path('logoutview',logoutview,name='logoutview'),
    path('findJobs',findJobs,name='findJobs'),
    path('trainerApplications/<int:pk>',trainerApplications,name='trainerApplications'),
    path('myapplications',myapplications,name='myapplications')

]
