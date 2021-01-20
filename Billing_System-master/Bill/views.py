from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from Bill.models import ProductModel, SalesModel, PurchaseModel, OrderModel
from Bill.forms import ProductForm, Purchaseform, SalesForm, OrderForm


class product(TemplateView):
    model = ProductModel
    template_name = "product.html"
    context = {}
    context_object_name = "products"

    def get(self, request, *args, **kwargs):
        form = ProductForm()
        products = self.model.objects.all()
        self.context["form"] = form
        self.context["products"] = products
        return render(request, self.template_name, self.context)

    def post(self, request, *args, **kwargs):
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("products")
        else:
            form = ProductForm(request.POST)
            products = self.model.objects.all()
            self.context["form"] = form
            self.context["products"] = products
            return render(request, self.template_name, self.context)


class EditProduct(TemplateView):
    model = ProductModel
    template_name = "product.html"
    context = {}
    context_object_name = "products"

    def get(self, request, *args, **kwargs):
        product = self.model.objects.get(id=kwargs["pk"])
        form = ProductForm(instance=product)
        products = self.model.objects.all()
        self.context["products"] = products
        self.context["form"] = form
        return render(request, self.template_name, self.context)

    def post(self, request, *args, **kwargs):
        product = self.model.objects.get(id=kwargs["pk"])
        form = ProductForm(instance=product, data=request.POST)
        if form.is_valid():
            form.save()
        return redirect("products")


class DeleteProduct(TemplateView):
    def get(self, request, *args, **kwargs):
        ProductModel.objects.get(id=kwargs["pk"]).delete()
        return redirect("products")


class Purchase(TemplateView):
    model = PurchaseModel
    template_name = "purchase.html"
    context = {}
    context_object_name = "purchases"

    def get(self, request, *args, **kwargs):
        purchases = self.model.objects.all()
        form = Purchaseform()
        self.context["form"] = form
        self.context["purchases"] = purchases
        return render(request, self.template_name, self.context)

    def post(self, request, *args, **kwargs):
        form = Purchaseform(request.POST)
        if form.is_valid():
            form.save()
            return redirect("purchases")
        else:
            form = Purchaseform(request.POST)
            purchases = self.model.objects.all()
            self.context['form'] = form
            self.context['purchases'] = purchases
            return render(request, self.template_name, self.context)


class EditPurchase(TemplateView):
    model = PurchaseModel
    template_name = "purchase.html"
    context = {}
    context_object_name = "purchases"

    def get(self, request, *args, **kwargs):
        purchase = self.model.objects.get(id=kwargs['pk'])
        form = Purchaseform(instance=purchase)
        self.context["form"] = form
        purchases = self.model.objects.all()
        self.context["purchases"] = purchases
        return render(request, self.template_name, self.context)

    def post(self, request, *args, **kwargs):
        purchase = self.model.objects.get(id=kwargs['pk'])
        form = Purchaseform(instance=purchase, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect("purchases")
        else:
            form = Purchaseform(request.POST)
            self.context["form"] = form
            purchases = self.model.objects.all()
            self.context["purchases"] = purchases
            return render(request, self.template_name, self.context)


class DeletePurchase(TemplateView):
    def get(self, request, *args, **kwargs):
        PurchaseModel.objects.get(id=kwargs["pk"]).delete()
        return redirect("purchases")


class Sales(TemplateView):
    model = SalesModel
    context = {}
    template_name = "sales.html"

    def get(self, request, *args, **kwargs):

        sale = self.model.objects.all().last()
        if sale:
            bill = sale.bill_number.lstrip("kly-")
            billnumber = "kly-" + str(int(bill) + 1)
            form = SalesForm(initial={'bill_number': billnumber})
            self.context["form"] = form
            return render(request, self.template_name, self.context)
        else:
            billnumber = 'kly-1000'
            form = SalesForm(initial={'bill_number': billnumber})
            self.context["form"] = form
            return render(request, self.template_name, self.context)

    def post(self, request, *args, **kwargs):
        form = SalesForm(request.POST)
        if form.is_valid():
            billnumber = form.cleaned_data.get("bill_number")
            form.save()
            return redirect("billing", pk=billnumber)


class Order(TemplateView):
    model = OrderModel
    template_name = "billing.html"
    context = {}

    def get(self, request, *args, **kwargs):
        form = OrderForm(initial={"bill_number": kwargs["pk"]})
        orders = self.model.objects.filter(bill_number=kwargs["pk"])
        self.context["form"] = form
        self.context["orders"] = orders
        return render(request, self.template_name, self.context)

    def post(self, request, *args, **kwargs):
        temp = request.POST.copy()
        qty = temp['quantity']
        pname = temp['product_name']
        s_price = PurchaseModel.objects.get(
            product_name__product_name=pname).selling_price
        price = int(s_price)*int(qty)
        temp['price'] = price
        temp['rate'] = s_price

        form = OrderForm(temp)
        if form.is_valid():
            form.save()

            billnumber = form.cleaned_data.get('bill_number')
            total = SalesModel.objects.get(bill_number=billnumber)
            total.bill_total += temp['price']
            total.save()

            purchaseobj = PurchaseModel.objects.get(
                product_name__product_name=pname)
            purchaseobj.quantity -= int(qty)
            purchaseobj.save()

            return redirect('billing', pk=billnumber)
        else:
            form = OrderForm(request.POST)
            orders = self.model.objects.filter(bill_number=kwargs["pk"])
            self.context["orders"] = orders
            self.context['form'] = form
            return render(request, self.template_name, self.context)


class DeleteOrder(TemplateView):
    def get(self, request, *args, **kwargs):

        temp = OrderModel.objects.get(id=kwargs["pk"])

        billnumber = temp.bill_number
        qty = temp.quantity
        pr = temp.price
        prod = temp.product_name

        purchaseobj = PurchaseModel.objects.get(
            product_name__product_name=prod)
        purchaseobj.quantity += int(qty)
        purchaseobj.save()

        total = SalesModel.objects.get(bill_number=billnumber)
        total.bill_total -= int(pr)
        total.save()

        OrderModel.objects.get(id=kwargs["pk"]).delete()

        return redirect("billing", pk=billnumber)
