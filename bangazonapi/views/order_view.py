from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import status
from bangazonapi.models.order import Order
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
