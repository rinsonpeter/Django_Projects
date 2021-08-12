from django.shortcuts import render
from rest_framework import serializers
from rest_framework.views import APIView
from rest_framework.response import Response

from Employee.models import ModelDept
from Employee.serializers import SerializerDept


# Create your views here.
class ViewDept(APIView):
    def get(self, request):
        qryset_dept=list(ModelDept.objects.all().values())
        # print("Qryset",qryset_dept)
        # serializer=SerializerDept(qryset_dept,many=True)
        # print("serializer:",serializer)
        # print("serializer.data: ",serializer.data)
        return Response(qryset_dept)
