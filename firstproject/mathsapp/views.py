from django.shortcuts import render


# Create your views here.
def getcalc(request):
    return render(request, "calculationPage.html")


def add(request):
    no1 = int(request.POST.get("no1"))
    no2 = int(request.POST.get("no2"))
    sum = no1 + no2
    return render(request, "calculationPage.html", {"add": sum})

def sub(request):
    no1 = int(request.POST.get("no1"))
    no2 = int(request.POST.get("no2"))
    sub = no1 - no2
    return render(request, "calculationPage.html", {"Minus": sub})

def mul(request):
    no1 = int(request.POST.get("no1"))
    no2 = int(request.POST.get("no2"))
    mult = no1 * no2
    return render(request, "calculationPage.html", {"multiply": mult})

def div(request):
    no1 = int(request.POST.get("no1"))
    no2 = int(request.POST.get("no2"))
    divv = no1 / no2
    return render(request, "calculationPage.html", {"Division": divv})
