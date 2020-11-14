from django.http import  HttpResponse
from django.shortcuts import render


def trainerlog(request):
    return render(request,"trainer_login.html")

def trainerreg(request):
    return render(request,"trainer_reg.html")

def sub(request):
    return HttpResponse("<h1>Inside SUB</h>")

def div(request):
    return HttpResponse("<h1>Inside divvv</h>")