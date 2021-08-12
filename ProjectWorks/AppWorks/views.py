from django.shortcuts import render
from rest_framework import serializers
from rest_framework.response import Response
from rest_framework.serializers import Serializer
from rest_framework.views import APIView
from .models import ModelWorks, ModelWorkStatus, ModelProject, ModelWorkTypes
from .serializers import SerializerWorks
from rest_framework import status

class ViewWorksGetPost(APIView):
    def get(self,request):
        res_data=ModelWorks.objects.all().values()
        #serilaizer=SerializerWorks(res_data,many=True)
        serializer=list(res_data)
        #return Response(serilaizer.data,status=status.HTTP_200_OK)
        return Response(serializer,status=status.HTTP_200_OK)

    def post(self,request):
        serilaizer=SerializerWorks(data=request.data)
        if serilaizer.is_valid():
            serilaizer.save()
            return Response(serilaizer.data, status=status.HTTP_201_CREATED)
        return Response(serilaizer.errors, status=status.HTTP_400_BAD_REQUEST)


class ViewWorkUpdateDelete(APIView):
    def get_queryset(self, id):
        return ModelWorks.objects.get(id=id)

    def get(self,request,id):
        res_data=self.get_queryset(id)
        serializer=SerializerWorks(res_data)
        print("res-data:",res_data)
        print("serializer:",serializer)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
        
    def put(self,request,id):
        res_data=self.get_queryset(id)
        serilaizer=SerializerWorks(res_data,data=request.data)
        if serilaizer.is_valid():
            serilaizer.save()
            return Response(serilaizer.data,status=status.HTTP_201_CREATED)
        return Response(serilaizer.errors,status=status.HTTP_400_BAD_REQUEST)

    def delete(self,request,id):
        rst_data=self.get_queryset(id)
        rst_data.delete()
        return Response("success")