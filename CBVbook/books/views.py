from django.shortcuts import render, redirect
from django.views.generic import ListView,\
    CreateView, DetailView, DeleteView, UpdateView,\
    TemplateView
from books.models import Book
from django.urls import reverse_lazy
from books.forms import BookCreateForm ,\
     UserRegistrationForm, LoginForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout

# Create your views here.


class ListBooks(TemplateView):
    model = Book
    template_name = 'books/book_list.html'

    def get(self, request, *args, **kwargs):
        context = {}
        context['books'] = self.model.objects.all()
        return render(request, self.template_name, context)


class CreateBooks(TemplateView):
    model = Book
    context = {}
    form_class = BookCreateForm()
    template_name = 'books/book_form.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class
        self.context['form'] = form
        return render(request, self.template_name, self.context)

    def post(self, request, *args, **kwargs):
        form = BookCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list')
        else:
            self.context['form'] = form
            return render(request, self.template_name, self.context)


class DetailBooks(TemplateView):
    model = Book
    template_name = 'books/book_detail.html'
    context = {}

    def get(self, request, *args, **kwargs):
        print(kwargs.get('pk'))
        book = self.model.objects.get(id=kwargs.get('pk'))
        self.context['object'] = book
        return render(request, self.template_name, self.context)


class DeleteBooks(DeleteView):
    model = Book
    # success_url = reverse_lazy('list')

    def get_queryset(self, pk):
        return self.model.objects.get(id=pk)

    def get(self, request, *args, **kwargs):
        book = self.get_queryset(kwargs.get('pk'))
        book.delete()
        return redirect('list')


class UpdateBooks(UpdateView):
    model = Book
    template_name = 'books/book_edit.html'
    context = {}
    # fields=['book_name','price','pages','author']
    # success_url=reverse_lazy('list')
 
    def get_queryset(self, pk):
        return self.model.objects.get(id=pk)

    def get(self, request, *args, **kwargs):
        book = self.get_queryset(kwargs.get('pk'))
        form = BookCreateForm(instance=book)
        self.context['form'] = form
        return render(request, self.template_name, self.context)

    def post(self, request, *args, **kwargs):
        form = BookCreateForm(instance=self.get_queryset(kwargs.get('pk')), data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('list')

class RegistrationView(TemplateView):
    template_name="books/registration.html"
    context={}

    def get(self, request, *args, **kwargs):
        form=UserRegistrationForm()
        self.context['form']=form
        return render(request,self.template_name,self.context)

    def post(self,request,*args,**kwargs):
        form=UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('SignIn')    

class SignIn(TemplateView):
    template_name='books/login.html'
    context={}

    def get(self,request,*args,**kwargs):
        form=LoginForm()
        self.context['form']= form
        return render(request,self.template_name,self.context)

    def post(self,request,*args,**kwargs):
        form=LoginForm(request.POST)
        if form.is_valid():
            username=form.cleaned_data.get('username')
            password=form.cleaned_data.get('password')
            user=authenticate(request,username=username,password=password)
            if (user):
                login(request,user)
                return redirect('list')
            else:
                self.context['form']=form
                return render(request,self.template_name,self.context)

class SignOut(TemplateView):
    def get(self,request,*args,**kwargs):
        logout(request)
        return redirect('SignIn')            




    
    