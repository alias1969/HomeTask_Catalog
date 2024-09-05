"""
URL configuration for config app.
"""
from tkinter.font import names
from xml.etree.ElementInclude import include

from django.contrib import admin
from catalog.apps import CatalogConfig
from django.urls import path
from catalog.views import home
from catalog.views import contacts

app_name = CatalogConfig.name

urlpatterns = [
    path('', home, name = 'home'),
    path('/contacts', contacts, name = 'contacts')
    ]


