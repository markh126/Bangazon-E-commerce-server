from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import status
from bangazonapi.models import OrderProduct, Product
from bangazonapi.serializers import OrderProductSerializer, ProductSerializer

class OrderProductView(ViewSet):
    """Bangazon Order View"""
    def retrieve(self, request, pk):
        """GET request for a single order product"""
        try:
            order_product = OrderProduct.objects.get(pk=pk)
            serializer = OrderProductSerializer(order_product)
            return Response(serializer.data)
        except OrderProduct.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)

    def list(self, request):
        """GET request for a list of products"""
        user_id = request.user.id  # Get the user's ID from the request
        products = Product.objects.filter(orderproduct__order_id__customer_id=user_id)
        for product in products:
            # Check if the user has joined the product by filtering OrderProduct instances
            product.joined = OrderProduct.objects.filter(product_id=product, order_id__customer_id=user_id).exists()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)