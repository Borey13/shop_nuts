from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=200)
    discription = models.TextField()
    price = models.FloatField()
    link_foto = models.TextField(default='link_foto')
    category_id = models.IntegerField()




    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'


class Category(models.Model):
    category_id = models.IntegerField()
    name = models.CharField(max_length=200)
    discription = models.TextField(default='discription')
    link_foto = models.TextField(default='link_foto')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

class ProductCalories(models.Model):
    name = models.CharField(max_length=200, default='name')
    calories = models.IntegerField()
    proteins = models.FloatField()
    fats = models.FloatField()
    carbohydrates = models.FloatField()

    def __str__(self):
        return self.name
    class Meta:
        verbose_name = 'БЖУ'
        verbose_name_plural = 'БЖУ'

