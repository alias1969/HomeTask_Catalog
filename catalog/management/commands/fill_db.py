from django.core.management import BaseCommand
import json
from catalog.models import Category, Product, Contacts


class Command(BaseCommand):
    """Класс для первоначального заполнения данных"""

    @staticmethod
    def json_read_data():
        """Для получения данных из фикстур"""
        with open("data/catalog_data.json", encoding="utf-8") as file:
            values = json.load(file)

        categories = [value for value in values if value["model"] == "catalog.category"]
        products = [
            value["fields"] for value in values if value["model"] == "catalog.product"
        ]
        contacts = [value["fields"] for value in values if value["model"] == "catalog.contacts"]

        return categories, products, contacts

    def handle(self, *args, **options):
        """Заполнить данные моделей Product и Category"""

        # удалим все данные
        Category.objects.all().delete()
        Product.objects.all().delete()
        Contacts.objects.all().delete()

        product_for_create = []
        contact_for_create = []

        # Получим контакты, категории и продукты из json
        categories, products, contacts = Command.json_read_data()

        #запишем контакты
        for contact in contacts:
            contact_for_create.append(Contacts(**contact))

        Contacts.objects.bulk_create(contact_for_create)


        # запишем данные категорий
        for category in categories:
            id = category.pop("pk")
            Category.objects.create(pk=id, **category["fields"])

        # запишем данные продуктов
        for product in products:
            id_category = product.pop("category")
            product_object = Product(
                category=Category.objects.get(pk=id_category), **product
            )

            product_for_create.append(product_object)

        Product.objects.bulk_create(product_for_create)
