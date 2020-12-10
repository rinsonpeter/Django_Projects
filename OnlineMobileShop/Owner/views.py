from django.shortcuts import render, redirect
from Owner.forms import BrandcreateForm, MobileCreationForm, OrderForm
from Owner.models import Brand,Mobile
from Users.models import Order


# Create your views here.
def index(request):
    return render(request,'owner/index.html')

def orderDetails(request, pk):
    orders = Order.objects.get(id = pk)
    form = OrderForm(instance = orders)
    context = {}
    context['form'] = form
    context['orders'] = orders
    if request.method == 'POST':
        form = OrderForm(data = request.POST, instance = orders)
        if form.is_valid():
            form.save()
            return redirect('viewOrders')

    return render(request, 'owner/orderdetails.html', context)


def viewOrders(request):    
    orders = Order.objects.all()
    context = {}
    context['orders'] = orders
    return render(request, 'owner/vieworders.html', context)


def createBrand(request):
    form = BrandcreateForm()
    brands = Brand.objects.all()
    context = {'form': form, 'brands': brands}
    template_name = 'owner/brandcreation.html'

    if request.method == "POST":
        form = BrandcreateForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, template_name, context)
        else:
            context['form'] = form
            return render(request, template_name, context)

    return render(request, template_name, context)


def deletebrands(request, pk):
    Brand.objects.get(id = pk).delete()
    return redirect('createbrand')


def updatebrand(request, pk):
    brand = Brand.objects.get(id = pk)
    form = BrandcreateForm(instance = brand)
    context = {'form': form}

    if request.method == 'POST':
        form = BrandcreateForm(instance = brand, data = request.POST)

        if form.is_valid():
            form.save()
            return redirect('createbrand')
        else:
            return render(request, 'owner/updatebrand.html', context)

    return render(request, 'owner/updatebrand.html', context)


def createMobile(request):
    form = MobileCreationForm()
    context = {}
    context['form'] = form
    if request.method == 'POST':
        form = MobileCreationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('listmobile')
        else:
            context['form'] = form
            return render(request, 'owner/createMobile.html', context)

    return render(request, 'owner/createMobile.html', context)


def listMobile(request):
    mobiles = Mobile.objects.all()
    context = {}
    context['mobiles'] = mobiles

    return render(request, 'owner/listmobile.html', context)


def viewMobiles(request, pk):
    qs = Mobile.objects.get(id = pk)
    context = {'mobile': qs}

    return render(request, 'owner/viewmobile.html', context)


def deleteMob(request, pk):
    Mobile.objects.get(id = pk).delete()
    return redirect('listmobile')


def updateMob(request, pk):
    mob = Mobile.objects.get(id = pk)
    form = MobileCreationForm(instance = mob)
    context = {}
    context['form'] = form

    if request.method == 'POST':
        form = MobileCreationForm(instance = mob, data = request.POST, files = request.FILES)
        if form.is_valid():
            form.save()
            print("inside update save")
            return redirect('listmobile')
        else:
            context['form'] = form
            return render(request, 'owner/updatemob.html', context)

    return render(request, 'owner/updatemob.html', context)
