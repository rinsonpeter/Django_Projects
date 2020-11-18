from django.contrib.auth import authenticate, login as djangologin, logout
from django.shortcuts import render, redirect
from patients.forms import PatientRegistrationForm, PatientLoginForm, PatientProfileForm
from django.contrib.auth.models import User


# Create your views here.


def patientRegistration(request):
    form = PatientRegistrationForm()
    context = {}
    context['form'] = form
    if request.method == 'POST':
        form = PatientRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('patientlogin')
        else:
            context['form'] = form
            return render(request, 'patients/patientregistration.html', context)

    return render(request, 'patients/patientregistration.html', context)


def patientLogin(request):
    print("inside patientlogin")
    form = PatientLoginForm()
    context = {}
    context['form'] = form
    if request.method == 'POST':
        form = PatientLoginForm(request.POST)
        if form.is_valid():
            print("allo")
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(request, username = username, password = password)
            if (user):
                djangologin(request,user)
                return redirect('patienthome')
            else:
                context['form'] = form
                return render(request, 'patients/patientlogin.html', context)

    return render(request, 'patients/patientlogin.html', context)

def patientHome(request):
    return render(request, 'patients/patienthome.html')

def createPatientProfile(request):
    form=PatientProfileForm(initial = {'user':request.user})
    context={}
    context['form']=form
    return render(request,'patients/patientprofile.html',context)