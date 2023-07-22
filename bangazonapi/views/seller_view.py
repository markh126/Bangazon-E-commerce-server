from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import status
from bangazonapi.models.seller import Seller
from bangazonapi.serializers.seller_serializer import SellerSerializer

class SellerView(ViewSet):
    """Bangazon Seller View"""
    def retrieve(self, request, pk):
        """GET request for a single seller"""
        try:
            sellers = Seller.objects.get(pk=pk)
            serializer = SellerSerializer(sellers)
            return Response(serializer.data)
        except Seller.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)

    def list(self, request):
        """GET request for a list of sellers"""
        sellers = Seller.objects.all()
        serializer = SellerSerializer(sellers, many=True, context={'request': request})
        return Response(serializer.data)
