from django import forms
from Books.models import Book
from django.forms import ModelForm


# class BookCreateForm(forms.Form):
#     book_name = forms.CharField(max_length = 120)
#     author = forms.CharField(max_length = 120)
#     price = forms.IntegerField()
#     pages = forms.IntegerField()

class BookCreateForm(ModelForm):
    class Meta:
        model = Book
        fields = "__all__"  # or ['modelfield1','modelfield2']
        widgets = {
            'book_name': forms.TextInput(attrs = {'class': "form-control"}),
            'author': forms.TextInput(attrs = {'class': "form-control"}),
            'price': forms.TextInput(attrs = {'class': "form-control"}),
            'pages': forms.TextInput(attrs = {'class': "form-control"}),
        }


    def clean(self):
        print("inside clean")
        cleaned_data = super().clean()
        bkname = cleaned_data.get('book_name')
        bk = Book.objects.filter(book_name = bkname)

        pr = cleaned_data.get('price')
        pg = cleaned_data.get('pages')
        print("inside clean")

        if (bk):
            msg = "This book already exists"
            self.add_error('book_name', msg)
        if (pr < 100):
            msg = "Minimum price is 100"
            self.add_error('price', msg)
        if (pg < 50):
            msg = "Minimum pages required is 100"
            self.add_error('pages', msg)
