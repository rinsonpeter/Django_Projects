from django.shortcuts import render, redirect
from student.models import Student


# Create your views here.
def student_log(request):
    return render(request, "student_login.html")


def student_reg(request):
    return render(request, "student_reg.html")


def getregdetails(request):
    email = request.POST.get("uname")
    pasw = request.POST.get("pasw")
    print("email: ", email)
    print("Password:", pasw)

    obj_stud = Student(stud_email=email, stud_pwd=pasw)
    obj_stud.save()
    print("object saved")
    return render(request, "student_login.html")

def chk_studlog(request):
    email = request.POST.get("st_uname")
    pasw = request.POST.get("st_psw")
    try:
        st_obj=Student.objects.get(stud_email=email)
        if(st_obj):
            psswd =st_obj.stud_pwd
            if(pasw==psswd):
                print("login success")
                return redirect("stud_home")
            else:
                return redirect("student_login.html")
    except:
        return redirect("student_login.html")

def stud_home(request):
    queryset = Student.objects.all()
    context = {}
    context["studs"] = queryset
    return render(request,"stud_home.html",context)



