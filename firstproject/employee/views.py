from django.shortcuts import render, redirect
from employee.models import Employee


# Create your views here.

def getregpage(request):
    return render(request, "emp_reg.html")


def emp_register(request):              #saves reg detail to db
    fname = request.POST.get("first")
    email = request.POST.get("email")
    uname = request.POST.get("username")
    pwd = request.POST.get("pwd")
    sal = request.POST.get("salary")
    obj = Employee(first = fname, email = email,uname = uname, pwd = pwd, sal = sal)
    obj.save()
    print("object saved")
    return render(request,"login.html")


def emp_login(request):
    email = request.POST.get("email")
    password = request.POST.get("pwd")
    try:
        empx = Employee.objects.get(email = email)
        if (empx):
            pswd = empx.pwd
            if (pswd == password):
                print("login success for employee")
                return redirect("home")
            else:
                return redirect("login.html")
    except:
        return redirect("login.html")

def emp_hom(request):
    return render(request,"login.html")



def empHome(request):
    print("inside emp Home page")
    queryset = Employee.objects.all()
    context = {}
    context["employees"] = queryset
    return render(request,"emp_home.html",context)



