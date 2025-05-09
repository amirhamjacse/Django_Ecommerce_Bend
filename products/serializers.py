from .models import Product
from rest_framework import serializers


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = [
            'category',
            'name',
            'description',
            'created_at',
        ]


class TestSeri(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields =[
            'category',
        ]