from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=200)
    discription = models.TextField()
    price = models.FloatField()
    category_id = models.IntegerField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'


class Category(models.Model):
    category_id = models.IntegerField()
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'