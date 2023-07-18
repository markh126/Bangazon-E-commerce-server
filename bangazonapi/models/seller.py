from django.db import models
from safedelete.models import SafeDeleteModel
from .customer import Customer

class Seller(SafeDeleteModel):
    customer_id = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True, related_name='customer')