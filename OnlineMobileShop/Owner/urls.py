from django.contrib import admin
from django.urls import path
from Owner.views import createBrand, deletebrands, updatebrand, createMobile, listMobile, viewMobiles, updateMob, \
    deleteMob, viewOrders, orderDetails,index

urlpatterns = [
    #    path('listbrands/',listBrands,name='listbrands'),
    path('index',index,name='index'),
    path('brandcreate/', createBrand, name = 'createbrand'),
    path("delete/<int:pk>", deletebrands, name = 'deletebrands'),
    path('update/<int:pk>', updatebrand, name = 'updatebrands'),
    path('createmobile/', createMobile, name = 'createmobile'),
    path('listmobile/', listMobile, name = 'listmobile'),
    path('view/<int:pk>', viewMobiles, name = 'viewmobiles'),
    path('updatemob/<int:pk>', updateMob, name = 'updatemob'),
    path('deletemob/<int:pk>', deleteMob, name = 'deletemob'),
    path('vieworders/', viewOrders, name = 'viewOrders'),
    path('orderdetails/<int:pk>', orderDetails, name = 'orderDetails'),


]
