from django.contrib.auth.models import AbstractUser
from django.db import models

from catalog.models import NULLABLE


class User(AbstractUser):
    """Класс пользователей"""

    #авторизация по email
    name = None
    email = models.EmailField(verbose_name='email', unique=True, help_text='Введите email')

    phone = models.CharField(max_length=35, verbose_name='телефон', help_text='Введите номер телефона', **NULLABLE)
    avatar = models.ImageField(upload_to='users/', verbose_name='аватар', **NULLABLE)
    country = models.CharField(max_length=50, verbose_name='страна', help_text='Введите страну', **NULLABLE)

    token = models.CharField(max_length=100, verbose_name='Token', **NULLABLE)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"

    def __str__(self):
        return f'{self.email}'