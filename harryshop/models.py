from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone
from datetime import timedelta

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100,default="")

    def __str__(self):
        return self.name

class Product(models.Model):
    product_category = models.ForeignKey(Category, on_delete=models.CASCADE,default="")
    product_name = models.CharField(max_length=100,default="")
    product_price=models.IntegerField(default=0)
    product_description = models.TextField(default="")
    product_image=models.ImageField(upload_to='shopp/images',default="")
    product_color=models.CharField(max_length=20,default="")
    def __str__(self):
        return self.product_name
class CartItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def priceofspeproduct(self):
        return self.product.product_price*self.quantity

    def __str__(self):
        return f"{self.user.username}'s {self.product} ({self.quantity})"
    


    