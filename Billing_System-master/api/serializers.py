from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from Bill.models import ProductModel, PurchaseModel


class ProductSerializer(ModelSerializer):
    class Meta:
        model = ProductModel
        fields = ["product_name","p_name"]


class PurchaseSerializer(ModelSerializer):
    p_name=serializers.RelatedField(source="product_name",
        queryset=PurchaseModel.objects.all())
    class Meta:
        model = PurchaseModel
        fields = ["product_name","p_name"]
