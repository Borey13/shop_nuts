from django.db import models
from django.urls import reverse


class Product(models.Model):
    name = models.CharField(max_length=200, verbose_name='Название')
    description = models.TextField(null=False, blank=True, verbose_name='Описание товара')
    price = models.DecimalField(default=0, max_digits=8, decimal_places=2, verbose_name='Цена')
    image = models.ImageField(upload_to='products/%Y/%m/%d', blank=True, verbose_name='Фото товара')
    category_id = models.IntegerField()

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('main:product', args=[self.id])

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'


class Category(models.Model):
    category_id = models.IntegerField()
    name = models.CharField(max_length=200, verbose_name='Название')
    description = models.TextField(default='description', verbose_name='Описание категории')
    image = models.ImageField(upload_to='categories/%Y/%m/%d', blank=True, verbose_name='Фото')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

