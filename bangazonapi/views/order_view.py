from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework import status
from bangazonapi.models import Order, Customer, Product, OrderProduct
from bangazonapi.serializers.order_serializer import OrderSerializer

class OrderView(ViewSet):
    """Bangazon Order View"""
    def retrieve(self, request, pk):
        """GET request for a single order"""
        try:
            orders = Order.objects.get(pk=pk)
            serializer = OrderSerializer(orders)
            return Response(serializer.data)
        except Order.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)

    def list(self, request):
        """GET request for a list of orders"""
        orders = Order.objects.all()
        serializer = OrderSerializer(orders, many=True, context={'request': request})
        return Response(serializer.data)

    def create(self, request):
        """POST request for creating am order"""
        customer = Customer.objects.get(pk=request.data["customer_id"])
        order = Order.objects.create(
            details = request.data["details"],
            payment_type = request.data["payment_type"],
            customer_id = customer
        )
        order.save()
        serializer = OrderSerializer(order)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def update(self, request, pk):
        """PUT request to update an order"""
        order = Order.objects.get(pk=pk)
        order.payment_type = request.data["payment_type"]
        order.save()
        return Response({'message: Order Payment Updated'}, status=status.HTTP_204_NO_CONTENT)

    @action(methods=['post'], detail=True)
    def add_to_order(self, request, pk):
        """POST action to add product to open order"""
        product = Product.objects.get(pk=request.data["product_id"])
        order = Order.objects.get(pk=pk)
        OrderProduct.objects.create(
            product_id = product,
            order_id = order
        )
        return Response({'message: Added to Order'}, status=status.HTTP_201_CREATED)

    @action(methods=['delete'], detail=True)
    def remove_from_order(self, request, pk):
        """DELETE action to remove a product from an open order"""
        product = Product.objects.get(pk=request.data["product_id"])
        order = Order.objects.get(pk=pk)
        cart_product = OrderProduct.objects.get(
            product_id = product,
            order_id = order
        )
        cart_product.delete()
        return Response({'message: Removed from Order'}, status=status.HTTP_204_NO_CONTENT)
