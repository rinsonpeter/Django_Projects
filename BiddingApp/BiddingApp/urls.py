
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('institution/',include('Institution.urls')),
    path('trainer/',include('Trainer.urls')),

]
