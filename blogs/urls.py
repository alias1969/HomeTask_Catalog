"""
URL configuration for config app.
"""

from django.urls import path

from blogs.apps import BlogsConfig
from blogs.views import BlogsListView, BlogsDetailView, BlogsCreateView, BlogsUpdateView, BlogsDeleteView
from django.conf.urls.static import static
from django.conf import settings

app_name = BlogsConfig.name

urlpatterns = [
    path('blogs', BlogsListView.as_view(), name='blogs_list'),
    path('blogs/<int:pk>/', BlogsDetailView.as_view(), name='blogs_detail'),
    path('blogs/create', BlogsCreateView.as_view(), name='blogs_create'),
    path('blogs/<int:pk>/update/', BlogsUpdateView.as_view(), name='blogs_update'),
    path('blogs/<int:pk>/delete/', BlogsDeleteView.as_view(), name='blogs_delete'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
