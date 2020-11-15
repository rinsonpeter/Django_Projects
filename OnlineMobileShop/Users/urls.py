
from django.contrib import admin
from django.urls import path
from Users.views import registraion, signIn, userviewMobiles, orderMobile, viewCart

urlpatterns = [
    path('register',registraion,name='register'),
    path('signin',signIn,name='signin'),
    path('order/<int:pk>',orderMobile,name='ordermobile'),
    path('userviewMobiles/<int:pk>',userviewMobiles,name='userviewMobiles'),
    path('cart',viewCart,name='cart'),

]
