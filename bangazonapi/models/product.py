from django.db import models
from .customer import Customer

class Product(models.Model):
    name = models.CharField(max_length=100)
    product_image_url = models.CharField(max_length=300)
    price = models.FloatField()
    product_info = models.CharField(max_length=500)
    created_on = models.DateField(auto_now_add=True)
    category = models.CharField(max_length=50)
    seller_id = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='sellerId')
    
    @property
    def joined(self):
        """Join"""
        return self.__joined

    @joined.setter
    def joined(self, value):
        self.__joined = value
