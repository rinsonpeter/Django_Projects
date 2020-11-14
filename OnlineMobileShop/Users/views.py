from django.shortcuts import render, redirect
from Users.forms import RegistrationForm
from django.contrib.auth import login,logout,authenticate

# Create your views here.

def signIn(request):
    print("inside signin")
    if request.method == 'POST':
        username=request.POST.get("uname")
        password=request.POST.get("pwd")
        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return render(request,'users/userhome.html')


    return render(request, 'users/login.html')


def registraion(request):
    form = RegistrationForm()
    context = {}
    context['form'] = form
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            print("inside validation")
            return redirect("signin")
        else:
            context['form'] = form
            print("inside valid else")
            return render(request, 'users/registration.html', context)

    return render(request, 'users/registration.html', context)
