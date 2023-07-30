from rest_framework import serializers
from bangazonapi.models import OrderProduct

class OrderProductSerializer(serializers.ModelSerializer):
    """JSON serializer for orders"""
    class Meta:
        model = OrderProduct
        fields = ('id',
                  'product_id',
                  'order_id'
                  )
        depth = 1