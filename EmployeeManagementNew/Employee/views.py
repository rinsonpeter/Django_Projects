from re import template
from django.shortcuts import redirect, render
from Employee.forms import FormDeptCreate, FormCreateEmp
from .models import ModelDept, ModelEmpolyee
# Create your views here.
def viewcreateDept(request):
    context={}
    template_name="dept/htmlCreateDept.html"
    form=FormDeptCreate()
    dept=ModelDept.objects.all()

    context['dept']=dept
    context['form']=form
    if request.method=="POST":
        form=FormDeptCreate(request.POST)
        if form.is_valid():
            form.save()
            return render(request,template_name,context)    
        else:
            context['form']=form
            return render(request,template_name,context)    

    return render(request,template_name,context)

def viewDeleteDept(request, pk):
    ModelDept.objects.get(id = pk).delete()
    return redirect('viewCreateDept')    

def viewUpdateDept(request,pk): 
    template_name="dept/htmlUpdateDept.html"  
    dep=ModelDept.objects.get(id=pk)
    form=FormDeptCreate(instance=dep)
    context={}
    context={'form':form}

    if request.method=="POST":
        form=FormDeptCreate(instance=dep,data=request.POST)
        if form.is_valid():
            form.save()
            return redirect("viewCreateDept")
        else:
            context['form'] = form
            return render(request,template_name,context)

    return render(request,template_name,context)        

def viewCreateEmp(request):
    template_name="dept/htmlCreateEmp.html"
    form=FormCreateEmp()
    emp=ModelEmpolyee.objects.all()
    
    context={}
    context["form"]=form
    context['emp']=emp

    if request.method=="POST":
        form=FormCreateEmp(request.POST)
        if form.is_valid():
            form.save()
            return redirect('viewCreateEmp')
        else:
            context['form']=form
            return render(request,template_name,context)    

    return render(request,template_name,context)

def viewDeleteEmp(request, pk):
    print("PK VAlue delete",pk)
    ModelEmpolyee.objects.get(id = pk).delete()
    return redirect('viewCreateEmp')

def viewUpdateEmp(request,pk):
    template_name='dept/htmlUpdateEmp.html'
    emp=ModelEmpolyee.objects.get(id=pk)
    form=FormCreateEmp(instance=emp)

    context={}
    context['form']=form

    if request.method=="POST":
        form=FormCreateEmp(instance=emp, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('viewCreateEmp')
        else:
            context['form']=form
            return render(request,template_name,context)

    return render(request,template_name,context)

