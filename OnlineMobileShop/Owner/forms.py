from django import forms
from Owner.models import Brand, Mobile
from django.forms import ModelForm
from Users.models import Order

class BrandcreateForm(ModelForm):
    class Meta:
        model = Brand
        fields = '__all__'
        widgets = {
            'brand_name': forms.TextInput(attrs = {'class': 'form-control'}),
        }

    def clean(self):
        print("perform clean")
        cleaned_data = super().clean()
        brand_nm = cleaned_data.get('brand_name')
        brand_check = Brand.objects.filter(brand_name = brand_nm)

        if (brand_check):
            print("inside check")
            msg = "This brand already exists"
            self.add_error('brand_name', msg)


class MobileCreationForm(ModelForm):
    class Meta:
        model = Mobile
        fields = '__all__'
        widgets = {
            'mob_name': forms.TextInput(attrs = {'class': 'form-control'}),
            'brand': forms.Select(attrs = {'class': 'form-control'}),
            'ram': forms.TextInput(attrs = {'class': 'form-control'}),
            'internal': forms.TextInput(attrs = {'class': 'form-control'}),
            'color': forms.TextInput(attrs = {'class': 'form-control'}),
            'screensize': forms.TextInput(attrs = {'class': 'form-control'}),
            'processor': forms.TextInput(attrs = {'class': 'form-control'}),
            'price': forms.TextInput(attrs = {'class': 'form-control'}),
            'image': forms.ClearableFileInput(attrs = {'class': 'form-control'})
        }
class OrderForm(ModelForm):
    class Meta:
        model=Order
        fields="__all__"
        widgets = {
            'mobile': forms.TextInput(attrs = {'class': 'form-control','readonly':'readonly'}),
            'user': forms.TextInput(attrs = {'class': 'form-control','readonly':'readonly'}),
            'quantity': forms.TextInput(attrs = {'class': 'form-control','readonly':'readonly'}),
            'address': forms.Textarea(attrs = {'class': 'form-control','readonly':'readonly'}),
            'status': forms.Select(attrs = {'class': 'form-control'}),
            'price': forms.TextInput(attrs = {'class': 'form-control','readonly':'readonly'}),
            }
