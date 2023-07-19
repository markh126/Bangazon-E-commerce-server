from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import status
from bangazonapi.models.product import Product
from bangazonapi.serializers.product_serializer import ProductSerializer

class ProductView(ViewSet):
    """Bangazon Product View"""
    def retrieve(self, request, pk):
        """GET request for a single product"""
        try:
            products = Product.objects.get(pk=pk)
            serializer = ProductSerializer(products)
            return Response(serializer.data)
        except Product.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)

    def list(self, request):
        """GET request for a list of products"""
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True, context={'request': request})
        return Response(serializer.data)