from django.core.cache import cache

from catalog.models import Product, Category
from config.settings import CACHE_ENABLED


def get_product_from_cache():
    """Кэширование вывода данных о продуктах"""
    product = Product.objects.all()
    # если кэш включен
    if CACHE_ENABLED:
        key = "product_list"
        product_cache = cache.get(key)
        # если в кэш не пусто
        if product_cache is not None:
            return product_cache
        # запомним кэш
        cache.set(key, product)
    # если кэш не включен
    return product


def get_categories_from_cache():
    """Получить список категорий"""
    categories = Category.objects.all()
    # если кэш включен
    if CACHE_ENABLED:
        key = "categories_list"
        categories_cache = cache.get(key)
        # если в кэш не пусто
        if categories_cache is not None:
            return categories_cache
        # запомним кэш
        cache.set(key, categories)
    # если кэш не включен
    return categories
