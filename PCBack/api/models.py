from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Category(models.Model):
    name = models.CharField(max_length=255)


class Product(models.Model):
    name = models.CharField(max_length=255)
    user = models.ForeignKey(to=User, on_delete=models.SET_NULL)
    description = models.TextField()
    price = models.FloatField()
    image = models.TextField()
    quantity = models.IntegerField()
    rating = models.FloatField()
    category_id = models.ForeignKey(to='Category', on_delete=models.CASCADE)


class Cart(models.Model):
    user = models.OneToOneRel(User, on_delete=models.CASCADE)


class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
