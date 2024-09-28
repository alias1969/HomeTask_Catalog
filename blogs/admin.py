from django.contrib import admin

from django.contrib import admin
from blogs.models import Blogs


@admin.register(Blogs)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("pk", "headline", "content")
