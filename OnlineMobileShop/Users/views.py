from django.shortcuts import render, redirect
from Users.forms import RegistrationForm, OrderForm
from django.contrib.auth import login, logout, authenticate
from Owner.models import Mobile
from Users.models import Order
from django.contrib.auth.decorators import login_required



def logoutview(request):
    logout(request)
    return redirect('signin')

@login_required(login_url ='signin')
def viewCartItem(request,pk):
    order=Order.objects.get(id=pk)
    context={}
    context['order']=order
    return render(request,'users/viewCartItem.html',context)

@login_required(login_url ='signin')
def deleteOrder(request, pk):
    Order.objects.get(id = pk).delete()
    return redirect('cart')

@login_required(login_url ='signin')
def viewCart(request):
    orders = Order.objects.filter(user = request.user)

    context = {}
    context['orders'] = orders
    return render(request, 'users/usercart.html', context)

@login_required(login_url ='signin')
def orderMobile(request, pk):
    mobile = Mobile.objects.get(id = pk)
    mobilename = mobile.mob_name
    form = OrderForm(initial = {'mobile': mobilename, 'user': request.user})
    context = {}
    context['form'] = form
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('cart')
        else:
            form = OrderForm(request.POST)
            context['form'] = form
            return render(request, 'users/ordermobile.html', context)

    return render(request, 'users/ordermobile.html', context)


@login_required(login_url ='signin')
def userviewMobiles(request, pk):
    qs = Mobile.objects.get(id = pk)
    context = {'mobile': qs}
    return render(request, 'users/userviewmob.html', context)

@login_required(login_url ='signin')
def userHome(request):
    mobiles = Mobile.objects.all()
    context = {}
    context['mobiles'] = mobiles
    return render(request, 'users/userhome.html', context)


def signIn(request):
    print("inside signin")
    if request.method == 'POST':
        username = request.POST.get("uname")
        password = request.POST.get("pwd")
        user = authenticate(request, username = username, password = password)
        if user is not None:
            login(request, user)
            return redirect('userhome')

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
