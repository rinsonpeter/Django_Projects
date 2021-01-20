from Bill.models import ProductModel, SalesModel, PurchaseModel, OrderModel
from django.forms import ModelForm
from django import forms


class ProductForm(ModelForm):
    class Meta:
        model = ProductModel
        fields = "__all__"
        widgets = {
            "product_name": forms.TextInput(attrs={'class': 'form-control'})
        }

    def clean(self):
        cleaned_data = super().clean()
        productname = cleaned_data.get("product_name")
        product = ProductModel.objects.filter(product_name=productname)
        if (product):
            msg = "product already exist"
            self.add_error('product_name', msg)


class Purchaseform(ModelForm):
    class Meta:
        model = PurchaseModel
        fields = ["product_name", "quantity", "buying_price", "selling_price"]
        widgets = {
            "product_name": forms.Select(attrs={'class': 'custom-select'}),
            "quantity": forms.NumberInput(attrs={'class': 'form-control'}),
            "buying_price": forms.NumberInput(attrs={'class': 'form-control'}),
            "selling_price": forms.NumberInput(attrs={'class': 'form-control'})
        }

    def clean(self):
        cleaned_data = super().clean()
        clean_quantity = int(cleaned_data.get("quantity"))
        clean_buying_price = int(cleaned_data.get('buying_price'))
        clean_selling_price = int(cleaned_data.get('selling_price'))

        if (clean_quantity <= 0):
            msg = "Minimun quantity 1 is required"
            self.add_error('quantity', msg)
        if (clean_buying_price <= 0):
            msg = "Minimun  price 1 is required"
            self.add_error('buying_price', msg)
        if (clean_selling_price <= 0):
            msg = "Minimun price 1 is required"
            self.add_error('selling_price', msg)


class SalesForm(ModelForm):
    class Meta:
        model = SalesModel
        fields = ['bill_number', 'customer_name', 'phone']
        widgets = {
            "bill_number": forms.TextInput(attrs={'class': 'form-control', 'readonly': 'readonly'}),
            "customer_name": forms.TextInput(attrs={'class': 'form-control'}),
            "phone": forms.NumberInput(attrs={'class': 'form-control'})
        }


class OrderForm(ModelForm):
    #bill_number = forms.CharField()
    purchase = PurchaseModel.objects.all().values_list(
        "product_name__product_name", flat=True).distinct()
    choice = [(name, name) for name in purchase]
    product_name = forms.ChoiceField(
        choices=choice, required=False,
        widget=forms.Select(attrs={'class': 'custom-select'}))

    class Meta:
        model = OrderModel
        fields = ['bill_number', 'product_name', 'quantity', 'rate', 'price']
        widgets = {
            "bill_number": forms.TextInput(attrs={'class': 'form-control', 'readonly': 'readonly'}),
            "quantity": forms.TextInput(attrs={'class': "form-control"}),
            "price": forms.HiddenInput(),
            "rate": forms.HiddenInput(),
            "price": forms.HiddenInput(),
        }

    def clean(self):
        cleaned_data = super().clean()
        prod = cleaned_data.get('product_name')
        qty = cleaned_data.get('quantity')
        temp = PurchaseModel.objects.get(product_name__product_name=prod)
        print(temp)
        if int(qty) > int(temp.quantity):
            msg = "Available quantity:"+str(temp.quantity)
            self.add_error('quantity', msg)
