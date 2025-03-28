from products.models import Product
from django.views.generic import (
    CreateView,
)
from rest_framework.views import APIView
from products.serializers import ProductSerializer
from rest_framework.response import Response
from rest_framework import status
from drf_yasg.utils import swagger_auto_schema


class ProductListAPI(APIView):
    # @swagger_auto_schema(request_body=ProductSerializer)
    def get(self, request):
        product_obj = Product.objects.all()
        serializer = ProductSerializer(product_obj, many=True)
        return Response(serializer.data)
