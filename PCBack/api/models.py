from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=255)


class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.FloatField()
    image = models.TextField()
    quantity = models.IntegerField()
    rating = models.FloatField()
    category_id = models.ForeignKey(to='Category', on_delete=models.CASCADE)


class Supplier(models.Model):
    name = models.CharField(max_length=255)
    rating = models.FloatField()
    product = models.ForeignKey(to='Product', on_delete=models.CASCADE)


class Delivery(models.Model):
    name = models.CharField(max_length=255)
    rating = models.FloatField()
    product = models.ForeignKey(to='Product', on_delete=models.CASCADE)


class Manager(models.Manager):
    pass
