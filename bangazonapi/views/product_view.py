from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import status
from bangazonapi.models.product import Product
from bangazonapi.models.seller import Seller
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

    def create(self, request):
        """POST request for creating a product"""
        seller = Seller.objects.get(pk=request.data["seller_id"])
        product = Product.objects.create(
            name = request.data["name"],
            product_image_url = request.data["product_image_url"],
            price = request.data["price"],
            product_info = request.data["product_info"],
            category = request.data["category"],
            seller_id = seller
        )
        product.save()
        serializer = ProductSerializer(product)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def update(self, request, pk):
        """PUT request to update a product"""
        product = Product.objects.get(pk=pk)
        product.name = request.data["name"]
        product.product_image_url = request.data["product_image_url"]
        product.price = request.data["price"]
        product.product_info = request.data["product_info"]
        product.category = request.data["category"]
        product.save()
        return Response({'message: Product Updated'}, status=status.HTTP_204_NO_CONTENT)

    def destroy(self, request, pk):
        """DELETE request to destroy a product"""
        product = Product.objects.get(pk=pk)
        product.delete()
        return Response({'message: Product DESTROYED'}, status=status.HTTP_204_NO_CONTENT)
        