# import serializer from rest_framework
from rest_framework import serializers

# import model from models.py
from .models import GeeksModel, ProductsModel


class GeeksSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = GeeksModel
        fields = ('title', 'description')


class ProductsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ProductsModel
        fields = ('id', 'title', 'description', 'barcode', 'price')
