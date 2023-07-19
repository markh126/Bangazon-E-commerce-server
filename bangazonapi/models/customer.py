from django.db import models

class Customer(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    profile_image_url = models.CharField(max_length=300)
    email = models.CharField(max_length=50)
    username = models.CharField(max_length=50)
    bio = models.CharField(max_length=300)
    seller = models.BooleanField(default=False)
    created_on = models.DateField(auto_now_add=True)
    uid = models.CharField(max_length=200)
    