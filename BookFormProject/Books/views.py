from django.shortcuts import render, redirect
from Books.forms import BookCreateForm
from Books.models import Book

# Create your views here.

def bookcreate(request):
    print("INSIDE BOOKCREATE")
    #    template_name = 'book_create.html'
    form = BookCreateForm()
    context = {'form': form}
    books = Book.objects.all()
    context['books'] = books

    if request.method == "POST":
        form = BookCreateForm(request.POST)
        if form.is_valid():
            form.save()
            # book_name = form.cleaned_data.get("book_name")
            # author = form.cleaned_data.get("author")
            # price = form.cleaned_data.get("price")
            # pages = form.cleaned_data.get("pages")
            #
            # obj = Book(book_name = book_name, author = author,
            #            price = price, pages = pages)
            # obj.save()
            qs = Book.objects.all()
            context['books'] = qs
            return render(request, 'book_create.html', context)
        else:
            context['form'] = form
            return render(request, 'book_create.html', context)

    return render(request, 'book_create.html', context)


def viewbooks(request, pk):
    qs = Book.objects.get(id = pk)
    context = {}
    context['book'] = qs
    return render(request, 'viewbooks.html', context)


def deletebooks(request, pk):
    Book.objects.get(id = pk).delete()
    return redirect('create')


def updatebooks(request, pk):
    book = Book.objects.get(id = pk)
    form = BookCreateForm(instance = book)
    context = {}
    context['form'] = form

    if request.method == 'POST':
        form = BookCreateForm(instance = book, data = request.POST)
        if form.is_valid():
            form.save()
            return redirect('create')
        else:
            context['form'] = form
            return render(request, 'updatebooks.html', context)

    return render(request, 'updatebooks.html', context)
