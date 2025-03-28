from django.db import models


class Categories(models.Model):
    name =  models.CharField(
        max_length=100, blank=True
        )
    description = models.TextField(
        null=True, blank=True
    )
    created_at = models.DateTimeField(auto_now=True)


class Product(models.Model):
    category = models.ForeignKey(
        Categories, on_delete=models.SET_NULL, blank=True, null=True
    )
    name =  models.CharField(
        max_length=100, blank=True
        )
    description = models.TextField(
        null=True, blank=True
    )
    created_at = models.DateTimeField(auto_now=True)


class ProductVarient(models.Model):
    products = models.ForeignKey(
        Product, on_delete=models.SET_NULL, null=True,
        blank=True
    )
    color_name = models.CharField(
        max_length=50, null=True, blank=True
    )
    color_code = models.CharField(
        max_length=50, null=True, blank=True
    )
    size = models.CharField(
        max_length=40, null=True, blank=True
    )
    quantity = models.CharField(
        max_length=10, null=True, blank=True
    )
    created_at = models.DateTimeField(auto_now=True)

# class StockHistory(model.Model):
