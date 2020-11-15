from django.shortcuts import render, redirect
from Users.forms import RegistrationForm,OrderForm
from django.contrib.auth import login,logout,authenticate
from Owner.models import Mobile

# Create your views here.
from Users.models import Order


def viewCart(request):
    orders=Order.objects.all()
    context={}
    context['orders']=orders
    return render(request,'users/usercart.html',context)

def orderMobile(request,pk):
    mobile=Mobile.objects.get(id=pk)
    mobilename=mobile.mob_name
    form=OrderForm(initial = {'mobile':mobilename,'user':request.user })
    context={}
    context['form']=form
    if request.method=='POST':
        form=OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('cart')
        else:
            form=OrderForm(request.POST)
            context['form']=form
            return render(request, 'users/ordermobile.html', context)

    return render(request,'users/ordermobile.html',context)

def userviewMobiles(request, pk):
    print("inside user view Mobiles")
    qs = Mobile.objects.get(id = pk)
    context = {'mobile': qs}
    return render(request,'users/userviewmob.html',context)



def signIn(request):
    print("inside signin")
    if request.method == 'POST':
        username=request.POST.get("uname")
        password=request.POST.get("pwd")
        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            mobiles = Mobile.objects.all()
            context = {}
            context['mobiles'] = mobiles
            return render(request, 'users/userhome.html', context)

    return render(request, 'users/login.html')


def registraion(request):
    form = RegistrationForm()
    context = {'form': form}
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
