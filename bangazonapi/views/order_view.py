from django.http import HttpResponseServerError
from django.shortcuts import get_object_or_404
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
    
    def destroy(self, request, pk):
        """DELETE request to destroy a product"""
        order = Order.objects.get(pk=pk)
        order.delete()
        return Response({'message: Order DESTROYED'}, status=status.HTTP_204_NO_CONTENT)

    @action(methods=['post'], detail=False)
    def add_to_cart(self, request, pk):
        """POST action to add product to open order"""
        # customer_id = request.data.get("customer_id")
        product_id = request.data.get("product_id")

        customer = get_object_or_404(Customer, pk=pk)
        order, _ = Order.objects.get_or_create(customer_id=customer, open=True)

        product = get_object_or_404(Product, pk=product_id)
        OrderProduct.objects.create(product_id=product, order_id=order)

        return Response({'message': 'Added to Order'}, status=status.HTTP_201_CREATED)

    @action(methods=['delete'], detail=False)
    def remove_from_cart(self, request, pk, product_id):
        """DELETE action to remove a product from an open order"""
        customer = get_object_or_404(Customer, pk=pk)
        order = get_object_or_404(Order, customer_id=customer, open=True)

        product = get_object_or_404(Product, pk=product_id)
        cart_products = OrderProduct.objects.filter(product_id=product, order_id=order)
        cart_products.delete()

        return Response({'message': 'Removed from Order'}, status=status.HTTP_204_NO_CONTENT)