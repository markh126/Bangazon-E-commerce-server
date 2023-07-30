from rest_framework import serializers
from bangazonapi.models.product import Product

class ProductSerializer(serializers.ModelSerializer):
    """JSON serializer for product"""
    class Meta:
        model = Product
        fields = ('id',
                  'name',
                  'price',
                  'product_info',
                  'product_image_url',
                  'category',
                  'created_on',
                  'seller_id',
                  'joined'
                  )
        depth = 1