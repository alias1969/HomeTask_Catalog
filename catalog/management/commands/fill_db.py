from django.core.management import BaseCommand
import json
import psycopg2
from catalog.models import Category, Product


class Command(BaseCommand):
    """ Класс для первоначального заполнения данных"""

    @staticmethod
    def json_read_data():
        """ Для получения данных из фикстур"""
        with open('data/catalog_data.json', encoding="utf-8") as file:
            values = json.load(file)

        categories = [value for value in values if value['model'] == "catalog.category"]
        products = [value['fields'] for value in values if value['model'] == "catalog.product"]

        return categories, products

    def handle(self, *args, **options):
        """ Заполнить данные моделей Product и Category"""

        # #сбросить инкрементацию для Catgories - чтобы по старым id найти категории для продуктов
        # with psycopg2.connect(database=os.getenv('name_database'), user=os.getenv('user_database'),
        #                       password=os.getenv('password_database')) as conn:
        #     with conn.cursor() as cur:
        #         cur.execute('TRUNCATE TABLE catalog_category RESTART IDENTITY CASCADE')
        #         conn.commit()

        # удалим все данные
        Category.objects.all().delete()
        Product.objects.all().delete()

        product_for_create = []
        category_for_create = []

        # Получим категории и продукты из json
        categories, products = Command.json_read_data()

        new_id = {}

        # запишем данные категорий
        for category in categories:
            id = category.pop('pk')
            Category.objects.create(pk = id, **category['fields'])
            #new_id[category['pk']] = category_object.pk
            #category_for_create.append(Category(**category))
        #Category.objects.bulk_create(category_for_create)


        # запишем данные продуктов
        for product in products:
            id_category = product.pop('category')
            product_object = Product(category=Category.objects.get(pk=id_category),**product)

            product_for_create.append(product_object)

        Product.objects.bulk_create(product_for_create)

