from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    
    path("works/",ViewWorksGetPost.as_view()),
    path("works/<int:id>",ViewWorkUpdateDelete.as_view())
]



