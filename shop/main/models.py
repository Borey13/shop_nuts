from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=200)
    discription = models.TextField()
    price = models.FloatField()
    category_id = models.IntegerField()

class Product(models.Model):
    category_id = models.IntegerField()
    name = models.CharField(max_length=200)
