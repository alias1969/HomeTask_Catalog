from django.forms import ModelForm

from blogs.models import Blogs


class ProductForm(ModelForm):
    """Форма продукта"""

    class Meta:
        model = Blogs
        exclude = (
            "created_at",
            "count_views",
        )