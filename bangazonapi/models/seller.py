from django.db import models
from .customer import Customer

class Seller(models.Model):
    customer_id = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='customer')