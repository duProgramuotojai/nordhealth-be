# import viewsets
from rest_framework import viewsets, filters, status, response

# import local data
from rest_framework.response import Response

from .serializers import GeeksSerializer, ProductsSerializer
from .models import GeeksModel, ProductsModel


class GeeksViewSet(viewsets.ModelViewSet):
    queryset = GeeksModel.objects.all()
    serializer_class = GeeksSerializer

    def add_to_cart(self, request, geek_id):
        geek = GeeksModel.objects.get(pk=geek_id)

        product = self.request.data.get('product')
        if product is not None:
            geek.shopping_cart.add(product)
            geek.save()
            return response.Response(status=status.HTTP_204_NO_CONTENT)

    def remove_from_cart(self, request, geek_id):
        geek = GeeksModel.objects.get(pk=geek_id)

        product = self.request.data.get('product')
        if product is not None:
            geek.shopping_cart.remove(product)
            geek.save()
            return response.Response(status=status.HTTP_204_NO_CONTENT)


class ProductsViewSet(viewsets.ModelViewSet):
    # define queryset ̰
    queryset = ProductsModel.objects.all()

    # specify serializer to be used
    serializer_class = ProductsSerializer

    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['title', 'barcode']
    ordering_fields = ['title']

    def perform_create(self, serializer):
        serializer.save()

    def partial_update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = ProductsSerializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def get_queryset(self):
        sorting_property = self.request.query_params.get('sort')
        order = self.request.query_params.get('order')
        products = ProductsModel.objects
        if sorting_property in ProductsSerializer.Meta.fields:
            products = products.order_by(sorting_property)
            if order == "desc":
                products = products.reverse()
        elif sorting_property is not None:
            print("sorting by invalid value: " + sorting_property)

        return products

    def destroy(self, *args, **kwargs):
        super().destroy(*args, **kwargs)
        return response.Response(status=status.HTTP_204_NO_CONTENT)

    def perform_destroy(self, instance):
        instance.delete()


