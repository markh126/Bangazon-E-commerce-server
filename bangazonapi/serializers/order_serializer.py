from rest_framework import serializers
from bangazonapi.models.order import Order

class OrderSerializer(serializers.ModelSerializer):
    """JSON serializer for orders"""
    class Meta:
        model = Order
        fields = ('id',
                  'date_placed',
                  'payment_type',
                  'open',
                  'customer_id'
                  )
        depth = 1