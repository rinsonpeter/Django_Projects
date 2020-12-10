from django.shortcuts import render,redirect
from Trainer.models import *
from Trainer.forms import *
from django.contrib.auth import *
from Institution.models import *
# Create your views here.

def trainerHome(request):
    return render(request,'trainerHome.html')

def trainerReg(request):
    form= TrainerRegForm()
    context={}
    context['form']= form
    if request.method=='POST':
        form=TrainerRegForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('trainerLogin')
        else:
            context['form']=form
            return render(request,'trainerReg.html',context)

    return render(request,'trainerReg.html',context)    

def trainerLogin(request):
    form = TrainerLoginForm()
    context = {}
    context['form'] = form
    if request.method == 'POST':
        form = TrainerLoginForm(request.POST)
        if form.is_valid():

            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(request, username=username, password=password)
            if (user):
                login(request, user)
                return redirect('trainerHome')
            else:
                context['form'] = form
                return render(request, 'trainerLogin.html', context)

    return render(request, 'trainerLogin.html', context)

def createTrainerProfile(request):
    form=TrainerCreationForm(initial={'user':request.user})
    context={}
    context['form']=form
    if request.method=='POST':
        form=TrainerCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('trainerHome')
        else:
            context['form']=form
            return render(request,'trainerProfile.html',context)

    return render(request,'trainerProfile.html',context)

def logoutview(request):
    logout(request)
    return redirect('trainerLogin')

def findJobs(request):
    qs=Jobs.objects.all()
    context={}
    context['qs']=qs
    return render(request,'joblist.html',context)

def trainerApplications(request,pk):
    skl=TrainerProfile.objects.get(user=request.user)
    skls=skl.skill

    titl=Jobs.objects.get(id=pk)
    titles=titl.jobTitle

    form=ApplicationForm(initial={'user': request.user,
                                 'skill': skls,
                                 'title':titles})
    context={}
    context['form']=form
    if request.method=='POST':
        form=ApplicationForm(request.POST)
        if form.is_valid():
            form.save()
            
            return redirect('myapplications')
        else:
            context['form']=form
            return render(request,'applyform.html',context)

    return render(request,'applyform.html',context)            

def myapplications(request):
    context={}
    apps=Applications.objects.filter(user=request.user)
    context['apps']=apps

    return render(request,'myapplications.html',context)    