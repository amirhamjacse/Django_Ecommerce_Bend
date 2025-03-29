from products.models import Product
from django.views.generic import (
    CreateView,
)
from rest_framework.views import APIView
from products.serializers import ProductSerializer
from rest_framework.response import Response
from rest_framework import status
from drf_yasg.utils import swagger_auto_schema
from django.core.cache import cache


class ProductListAPI(APIView):
    def get(self, request):
        cache_key = 'product_list'
        cache_data = cache.get(cache_key)

        if cache_data:
            print('caches')
            return Response(cache_data)


        product_obj = Product.objects.all()
        print('query')
        if not product_obj.exists():  # Check if there are no products
            return Response({"message": "No products found"}, status=status.HTTP_404_NOT_FOUND)
        serializer = ProductSerializer(product_obj, many=True)

        cache.set(cache_key, serializer.data, timeout=9000)
        print('other')
        return Response(serializer.data)

