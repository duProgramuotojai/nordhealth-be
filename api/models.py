# Create your models here.
from django.db import models


class ProductsModel(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()

    barcode = models.CharField(max_length=48)
    price = models.FloatField()

    def __str__(self):
        return self.title


class GeeksModel(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    shopping_cart = models.ManyToManyField(ProductsModel, blank=True, related_name='geeks', through='Cart')

    def __str__(self):
        return self.name


class Cart(models.Model):
    geek = models.ForeignKey(GeeksModel, on_delete=models.CASCADE)
    product = models.ForeignKey(ProductsModel, on_delete=models.CASCADE)
    count = models.IntegerField()
