from django.db import models
from safedelete.models import SafeDeleteModel

class Customer(SafeDeleteModel):
    deleted_by_cascade = None
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    profile_image_url = models.CharField(max_length=300)
    email = models.CharField(max_length=50)
    username = models.CharField(max_length=50)
    bio = models.CharField(max_length=300)
    seller = models.BooleanField(default=False)
    uid = models.CharField(max_length=200)
    