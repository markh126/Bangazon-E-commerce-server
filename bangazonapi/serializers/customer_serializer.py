from rest_framework import serializers
from bangazonapi.models.customer import Customer

class CustomerSerializer(serializers.ModelSerializer):
    """JSON serializer for customers"""
    class Meta:
        model = Customer
        fields = ('id',
                  'first_name',
                  'last_name',
                  'bio',
                  'profile_image_url',
                  'email',
                  'username',
                  'created_on',
                  'uid')
        depth = 1