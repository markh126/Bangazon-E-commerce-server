from rest_framework import serializers
from bangazonapi.models.seller import Seller

class SellerSerializer(serializers.ModelSerializer):
    """JSON serializer for sellers"""
    class Meta:
        model = Seller
        fields = ('id',
                  'customer_id'
                  )
        depth = 1