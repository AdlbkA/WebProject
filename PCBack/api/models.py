from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    id = models.AutoField(primary_key=True, editable=True)
    name = models.CharField(max_length=255)

    def __str__(self):
        return "Category: " + self.name

    def to_json(self):
        return {
            "id": self.id,
            "name": self.name,
        }


class Product(models.Model):
    name = models.CharField(max_length=255)
    id = models.AutoField(primary_key=True, editable=True)
    description = models.TextField()
    price = models.FloatField()
    image = models.TextField(null=True)
    quantity = models.IntegerField()
    rating = models.FloatField()
    category_id = models.ForeignKey(to='Category', on_delete=models.CASCADE)

    def __str__(self):
        return "Product: " + self.name

    def to_json(self):
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description,
            "price": self.price,
            "quantity": self.quantity,
            "rating": self.rating,
            "category": self.category.to_json() if self.category else None
        }


class Cart(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='cart')

    def __str__(self):
        return f"Cart for {self.user.username}"


class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return f"{self.quantity} of {self.product.name}"
