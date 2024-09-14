from django.db import models


NULLABLE = {'blank' : True, 'null' : True}

class Product(models.Model):
    """ Класс модели продуктов"""
    name = models.CharField(max_length=100, verbose_name='Наименование', help_text='Введите название продукта')
    description = models.TextField(max_length=1000, verbose_name='Описание', help_text='Введите описание продукта', ** NULLABLE)
    image = models.ImageField(
        upload_to='products/',
        verbose_name='Изображение (превью)',
        help_text='Добавьте изображение продукта',
        ** NULLABLE
    )
    category = models.ForeignKey(
        'Category',
        on_delete=models.SET_NULL,
        verbose_name='Категория',
        related_name='products',
        **NULLABLE
    )
    price = models.IntegerField(verbose_name='Цена за покупку', help_text='Введите цену', **NULLABLE)
    created_at = models.DateField(auto_now_add=True, verbose_name='Дата создания')
    updated_at = models.DateField(auto_now=True, verbose_name='Дата последнего изменения')
    #manufactured_at = models.DateField(verbose_name='Дата производства продукта', help_text='Введите дату производства', **NULLABLE)

    def __str__(self):
        return (
            f'{self.name}{self.description}{self.category}{self.price}'
            f'{self.created_at}{self.updated_at}'
        )

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
        ordering = ['category', 'name']


class Category(models.Model):
    """ Класс модели категории продуктов"""
    name = models.CharField(max_length=50, verbose_name='Наименование категории', help_text='Введите название категории')
    description = models.TextField(max_length=1000, verbose_name='Описание категории', help_text='Введите описание категории', **NULLABLE)

    def __str__(self):
        return f'{self.name}{self.description}'

    class Meta:
        verbose_name = 'Категория продукта'
        verbose_name_plural = 'Категории'
        ordering = ['name']


class Contacts(models.Model):
    """ Класс для хранения контактных данных"""
    type_contact = models.CharField(max_length=100, verbose_name='Тип контактных данных', help_text='Введите тип контактных данных')
    value_contact = models.CharField(max_length=150, verbose_name='Значение контактных данных', help_text='Введите значение контактных данных')

    def __str__(self):
        return f'{self.type_contact}{self.value_contact}'

    class Meta:
        verbose_name = 'Контактные данные'
        verbose_name_plural = 'Контактные данные'
