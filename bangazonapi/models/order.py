from django.db import models
from .customer import Customer

class Order(models.Model):
    order_number = models.IntegerField()
    details = models.CharField(max_length=300)
    date_placed = models.DateField()
    payment_type = models.CharField(max_length=50)
    open = models.BooleanField(default=True)
    customer_id = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True, related_name='customer_order')
    