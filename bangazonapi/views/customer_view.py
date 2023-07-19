from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import status
from bangazonapi.models.customer import Customer
from bangazonapi.serializers.customer_serializer import CustomerSerializer

class CustomerView(ViewSet):
    """Bangazon Customer View0"""
    def retrieve(self, request, pk):
        """GET request for a single customer"""
        try:
            customers = Customer.objects.get(pk=pk)
            serializer = CustomerSerializer(customers)
            return Response(serializer.data)
        except Customer.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)

    def list(self, request):
        """GET request for list of customers"""
        customers = Customer.objects.all()
        serializer = CustomerSerializer(customers, many=True, context={'request': request})
        return Response(serializer.data)
