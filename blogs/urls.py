"""
URL configuration for config app.
"""

from django.urls import path

from blogs.apps import BlogsConfig
from blogs.views import (
    BlogsListView,
    BlogsDetailView,
    BlogsCreateView,
    BlogsUpdateView,
    BlogsDeleteView,
    toggle_published,
)
from django.conf.urls.static import static
from django.conf import settings

app_name = BlogsConfig.name

urlpatterns = [
    path("blogs", BlogsListView.as_view(), name="blogs_list"),
    path("<int:pk>/", BlogsDetailView.as_view(), name="blogs_detail"),
    path("create", BlogsCreateView.as_view(), name="blogs_create"),
    path("<int:pk>/update/", BlogsUpdateView.as_view(), name="blogs_update"),
    path("<int:pk>/delete/", BlogsDeleteView.as_view(), name="blogs_delete"),
    path("<int:pk>/published", toggle_published, name="blogs_published"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
