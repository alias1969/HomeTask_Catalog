"""
URL configuration for config app.
"""

from django.urls import path
from catalog.views import home, contacts, ProductListView, ContactsTemplateView
from catalog.apps import CatalogConfig
from django.conf.urls.static import static
from django.conf import settings

app_name = CatalogConfig.name

urlpatterns = [
    path('', home, name="home"),
    #path('contacts/', ContactsTemplateView.as_view(), name='contacts'),
    path("contacts/", contacts, name="contacts"),
    #path('', ProductListView.as_view(), name='product_list'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
