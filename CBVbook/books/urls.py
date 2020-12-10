
from django.contrib import admin
from django.urls import path
from books.views import ListBooks,\
    CreateBooks,DetailBooks,DeleteBooks,UpdateBooks

urlpatterns = [
     path('',ListBooks.as_view(),name='list'),
     path('create',CreateBooks.as_view(),name='create'),
     path('details/<int:pk>',DetailBooks.as_view(),name='details'),
     path('delete/<int:pk>',DeleteBooks.as_view(),name='delete'),
     path('update/<int:pk>',UpdateBooks.as_view(),name='update'),
             
]
