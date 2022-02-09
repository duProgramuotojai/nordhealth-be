from django.db import models

# Create your models here.
from django.db import models


class GeeksModel(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()

    def __str__(self):
        return self.title


class ProductsModel(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()

    barcode = models.CharField(max_length=48)
    price = models.FloatField()

    def __str__(self):
        return self.title
