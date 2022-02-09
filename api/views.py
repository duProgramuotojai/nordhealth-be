from django.shortcuts import render
# import viewsets
from rest_framework import viewsets, filters, generics, status, response

# import local data
from rest_framework.response import Response

from .serializers import GeeksSerializer, ProductsSerializer
from .models import GeeksModel, ProductsModel


# create a viewset
class GeeksViewSet(viewsets.ModelViewSet):
    # define queryset
    queryset = GeeksModel.objects.all()

    # specify serializer to be used
    serializer_class = GeeksSerializer


class ProductsViewSet(viewsets.ModelViewSet):
    # define queryset ̰
    queryset = ProductsModel.objects.all()

    # specify serializer to be used
    serializer_class = ProductsSerializer

    filter_backends = [filters.SearchFilter]
    search_fields = ['title', 'barcode']

    def perform_create(self, serializer):
        serializer.save()

    def partial_update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = ProductsSerializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def get_queryset(self):
        return ProductsModel.objects

    def destroy(self, *args, **kwargs):
        super().destroy(*args, **kwargs)
        return response.Response(status=status.HTTP_204_NO_CONTENT)

    def perform_destroy(self, instance):
        instance.delete()


