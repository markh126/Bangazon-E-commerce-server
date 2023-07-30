# from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import status
from bangazonapi.models import Product, Customer, OrderProduct, Order
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
        seller_id = request.query_params.get('sellerId', None)
        if seller_id is not None:
            products = products.filter(seller_id=seller_id)
        for product in products:
            # Check to see if there is a row in the Event Games table that has the passed in gamer and event
            product.joined = len(OrderProduct.objects.filter(
                product_id=product)) > 0
        serializer = ProductSerializer(products, many=True, context={'request': request})
        return Response(serializer.data)

    def create(self, request):
        """POST request for creating a product"""
        seller = Customer.objects.get(uid=request.META['HTTP_AUTHORIZATION'])
        product = Product.objects.create(
            name = request.data["name"],
            product_image_url = request.data["productImageUrl"],
            price = request.data["price"],
            product_info = request.data["productInfo"],
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
        product.product_image_url = request.data["productImageUrl"]
        product.price = request.data["price"]
        product.product_info = request.data["productInfo"]
        product.category = request.data["category"]
        product.save()
        return Response({'message: Product Updated'}, status=status.HTTP_204_NO_CONTENT)

    def destroy(self, request, pk):
        """DELETE request to destroy a product"""
        product = Product.objects.get(pk=pk)
        product.delete()
        return Response({'message: Product DESTROYED'}, status=status.HTTP_204_NO_CONTENT)
        