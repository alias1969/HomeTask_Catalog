from django.db import models

from catalog.models import NULLABLE


class Blogs(models.Model):
    """Класс для хранения блоговой записи"""

    headline = models.CharField(
        max_length=150,
        verbose_name="Заголовок",
        help_text="Введите заголовок",
    )

    slug = models.CharField(
        max_length=150,
        verbose_name="Slug",
        help_text="Введите slug",
    )

    content = models.TextField(
        verbose_name="Содержимое",
        help_text="Введите содержимое",
        **NULLABLE,
    )

    preview = models.ImageField(
        upload_to="blogs/",
        verbose_name="Изображение (превью)",
        help_text="Добавьте превью",
        **NULLABLE,
    )

    created_at = models.DateField(auto_now_add=True, verbose_name="Дата создания")

    is_published = models.BooleanField(verbose_name="Опубликовано", default=False)

    count_views = models.IntegerField(verbose_name="Просмотров", default=0, **NULLABLE)

    def __str__(self):
        return f"{self.headline}"

    class Meta:
        verbose_name = "Блог"
        verbose_name_plural = "Блоги"
        permissions = [
            ("can_publish", "Can publish"),
        ]
