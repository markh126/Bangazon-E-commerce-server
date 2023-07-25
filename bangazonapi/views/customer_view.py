from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import status
from bangazonapi.models.customer import Customer
from bangazonapi.serializers.customer_serializer import CustomerSerializer

class CustomerView(ViewSet):
    """Bangazon Customer View"""
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

    def update(self, request, pk):
        """PUT request to update a customer"""
        customer = Customer.objects.get(pk=pk)
        uid = request.META["HTTP_AUTHORIZATION"]
        customer.first_name = request.data['firstName']
        customer.last_name = request.data['lastName']
        customer.bio = request.data['bio']
        customer.profile_image_url = request.data['profileImageUrl']
        customer.email = request.data['email']
        customer.username = request.data['userName']
        customer.uid = uid
        customer.save()
        return Response({'message': 'Customer Updated'}, status=status.HTTP_204_NO_CONTENT)

    def destroy(self, request, pk):
        """DELETE request to destroy a customer"""
        customer = Customer.objects.get(pk=pk)
        customer.delete()
        return Response({'message': 'Customer DESTROYED'}, status=status.HTTP_204_NO_CONTENT)
