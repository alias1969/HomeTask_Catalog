"""
URL configuration for config app.
"""

from django.urls import path
from catalog.views import home, contacts, product_detail, product_list, product_input
from catalog.apps import CatalogConfig
from django.conf.urls.static import static
from django.conf import settings

app_name = CatalogConfig.name

urlpatterns = [
    path("home", home, name="home"),
    path("contacts/", contacts, name="contacts"),
    path("", product_list, name="product_list"),
    path("products/<int:pk>/", product_detail, name="product_detail"),
    path("new_product/", product_input, name="product_input"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
