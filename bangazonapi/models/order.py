from django.db import models
from .customer import Customer

class Order(models.Model):
    date_placed = models.DateField(auto_now_add=True)
    payment_type = models.CharField(max_length=50)
    open = models.BooleanField(default=True)
    customer_id = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='customer_order')
