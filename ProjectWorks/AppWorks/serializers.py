from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from .models import *


class SerializerWorks(ModelSerializer):
    class Meta:
        model=ModelWorks
        fields="__all__"