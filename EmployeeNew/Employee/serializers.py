from django.db import models
from django.db.models import fields
from django.db.models.base import ModelState
from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from Employee.models import ModelDept

class SerializerDept(ModelSerializer):
    class Meta:
        model=ModelDept
        fields="__all__"

        
