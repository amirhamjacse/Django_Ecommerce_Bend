from django.urls import path
from products.views import (
    ProductListAPI
)


urlpatterns = [
    path('list/',
         ProductListAPI.as_view(),
         name='products_list'
         ),
]
