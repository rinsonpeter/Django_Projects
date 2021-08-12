from django.shortcuts import render
from django.views.generic import TemplateView

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import serializers, status

from Employee.models import ModelDept, ModelEmpolyee
from ApiEmployee.serializers import SerializerDept


class ViewDept(APIView):
    def get(self, request):
        # qryset_dept=ModelDept.objects.all()
        # print("Qryset",qryset_dept)
        # serializer=SerializerDept(qryset_dept,many=True)
        # print(serializer)
        # print(serializer.data)
        return Response("Success")

