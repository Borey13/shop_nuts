from django.contrib.auth.models import User
from django.db import models
from main.models import Product


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=50, verbose_name='Имя')
    last_name = models.CharField(max_length=50, verbose_name='Фамилия')
    email = models.EmailField()
    mobile = models.CharField(max_length=12, verbose_name='Телефон')
    city = models.CharField(max_length=50, verbose_name='Город')
    address = models.CharField(max_length=250, verbose_name='Адрес')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Создан')

    class Meta:
        ordering = ('-created',)
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'

    def __str__(self):
        return 'Заказ {}'.format(self.id)


class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, related_name='order_items', on_delete=models.CASCADE, verbose_name='Название')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Цена')
    quantity = models.PositiveIntegerField(default=1, verbose_name='Количество')
    total_price = models.DecimalField(max_digits=10, decimal_places=2, default=0, verbose_name='Общая стоимость')

    def __str__(self):
        return '{}'.format(self.order)

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Детали заказа'

