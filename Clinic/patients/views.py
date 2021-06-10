from django.contrib.auth import authenticate, login as djangologin, logout
from django.shortcuts import render, redirect
from patients.forms import *
from django.contrib.auth.models import User
from patients.models import PatientProfile


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
    form = PatientLoginForm()
    context = {}
    context['form'] = form
    if request.method == 'POST':
        form = PatientLoginForm(request.POST)
        if form.is_valid():
            print("allo")
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(request, username=username, password=password)
            print(user)
            if (user):
                print("iside usr")
                djangologin(request, user)
                return redirect('patienthome')
            else:
                context['form'] = form
                return render(request, 'patients/patientlogin.html', context)

    return render(request, 'patients/patientlogin.html', context)


def patientHome(request):
    return render(request, 'patients/patienthome.html')


def createPatientProfile(request):
    form = PatientProfileForm(initial={'user': request.user})
    context = {}
    context['form'] = form
    if request.method == 'POST':
        form = PatientProfileForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("patienthome")
        else:
            context['form'] = form
            return render(request, 'patients/patientprofile.html', context)
    return render(request, 'patients/patientplrofile.html', context)


def patientEditProfile(request):
    patient = PatientProfile.objects.get(user=request.user)
    form = PatientProfileForm(instance=patient)
    context = {}
    context['form'] = form

    if request.method == 'POST':
        form = PatientProfileForm(instance=patient, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('patienthome')
        else:
            context['form'] = form
            return render(request, 'patients/patienteditprofile.html', context)

    return render(request, 'patients/patienteditprofile.html', context)


def BookSlot(request):
    form = BookingForm(initial={'user': request.user})
    context = {}
    context['form'] = form
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('patienthome')
        else:
            context['form'] = form
            return render(request, 'patients/slotbooking.html', context)

    return render(request, 'patients/slotbooking.html', context)
