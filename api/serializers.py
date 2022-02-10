from rest_framework import serializers

from .models import GeeksModel, ProductsModel


class GeeksSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = GeeksModel
        fields = ('name', 'description', 'shopping_cart')


class ProductsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ProductsModel
        fields = ('id', 'title', 'description', 'barcode', 'price')

