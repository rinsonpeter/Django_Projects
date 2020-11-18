
from django.contrib import admin
from django.urls import path
from Users.views import registraion, signIn, userviewMobiles, orderMobile, viewCart, deleteOrder, viewCartItem, \
    logoutview,userHome

urlpatterns = [
    path('register',registraion,name='register'),
    path('',signIn,name='signin'),
    path('userhome',userHome,name='userhome'),
    path('order/<int:pk>',orderMobile,name='ordermobile'),
    path('userviewMobiles/<int:pk>',userviewMobiles,name='userviewMobiles'),
    path('cart',viewCart,name='cart'),
    path('deleteOrder/<int:pk>',deleteOrder,name='deleteOrder'),
    path('viewCartItem/<int:pk>',viewCartItem,name='viewCartItem'),
    path('logoutview',logoutview,name='logoutview'),


]
