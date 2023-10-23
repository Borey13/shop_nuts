from django.contrib.auth.models import User
from django.db import models


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name='Пользователь')
    mobile = models.CharField(max_length=12, verbose_name='Телефон', null=True, blank=False)
    city = models.CharField(max_length=50, verbose_name='Город', null=True, blank=False)
    created = models.DateTimeField(auto_now_add=True, verbose_name='Создан', null=True, blank=True)

    class Meta:
        verbose_name = 'Профиль пользователя'
        verbose_name_plural = 'Профили пользователей'

    def __str__(self):
        return str(self.user)

