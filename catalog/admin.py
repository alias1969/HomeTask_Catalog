from django.contrib import admin


from catalog.models import Product, Category, Contacts


# Зарегистрируйте свои модели здесь.


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price', 'category')
    list_filter = ('category',)
    search_fields = ('name', 'description')


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')


@admin.register(Contacts)
class ContactsAdmin(admin.ModelAdmin):
    list_display = ('type_contact', 'value_contact')

