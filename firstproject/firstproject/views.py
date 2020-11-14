from django.http import  HttpResponse

def home(request):
    return HttpResponse("<a href='http://127.0.0.1:8000/mathsapp/getcalc/'>Maths</a>")

def add(request):
    return HttpResponse("<h1>Inside add</h>")

def sub(request):
    return HttpResponse("<h1>Inside SUB</h>")

def div(request):
    return HttpResponse("<h1>Inside divvv</h>")