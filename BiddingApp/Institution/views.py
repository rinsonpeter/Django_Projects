from django.shortcuts import render, redirect
from Institution.forms import SkillCreationForm,JobCreationForm
from Institution.models import *

# Create your views here.


def home(request):
    form = SkillCreationForm()
    skl = Skills.objects.all()
    context = {'form': form, 'skl': skl}

    if request.method == 'POST':
        form = SkillCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'InstituteHome.html', context)
        else:
            context['form'] = form
            return render(request, 'InstituteHome.html', context)

    return render(request, 'InstituteHome.html', context)


def deleteSkills(request, pk):
    Skills.objects.get(id=pk).delete()
    return redirect('home')


def updateSkills(request, pk):
    skl = Skills.objects.get(id=pk)
    form = SkillCreationForm(instance=skl)
    context = {'form': form}

    if request.method == 'POST':
        form = SkillCreationForm(instance=skl, data=request.POST)

        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            return render(request, 'updateSkills.html', context)

    return render(request, 'updateSkills.html', context)

def createJobs(request):
    form=JobCreationForm()
    context={}
    context['form']=form
    if request.method=='POST':
        form=JobCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listJobs')
        else:
            context['form']= form
            return render(request,'createJobs.html',context)

    return render(request,'createJobs.html',context)        

def listJobs(request):
    job=Jobs.objects.all()
    context={}
    context['job']=job

    return render(request,'listJobs.html',context)

def deleteJobs(request, pk):
    Jobs.objects.get(id=pk).delete()
    return redirect('listJobs')
    