from django.db import models

from api.category .models import Category

import uuid

# Create your models here.


class Product(models.Model):
    id = models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True)
    name = models.CharField(max_length=200, null=False, blank=False)
    description = models.CharField(max_length=2000, null=False, blank=False)
    price = models.DecimalField(max_digits=50, decimal_places=3, default=100.0)
    stock = models.IntegerField(default=0)
    is_available = models.BooleanField(default=True, blank=True)
    image = models.ImageField(upload_to="product_images/", null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True) 
    uptated_at = models.DateTimeField(auto_now=True) 


    def __str__(self) -> str:
        return f"{self.name}"

