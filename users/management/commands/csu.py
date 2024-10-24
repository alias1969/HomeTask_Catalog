from django.core.management import BaseCommand
from users.models import User

class Command(BaseCommand):
    """Команда создания суперюзера"""

    def handle(self, *args, **options):
        # создаем суперпользователя
        user = User.objects.create(
            email='admin@sky.pro',
            first_name='Admin',
            last_name='Skystore',
        )

        user.is_staff = True
        user.is_superuser = True
        user.is_active = True
        user.set_password('123')  # for alias: HnapbTEC
        user.save()

        # создаем модератора продуктов
        user = User.objects.create(
            email='moderator@sky.pro',
            first_name='Product',
            last_name='Moderator',
        )
        user.is_staff = True
        user.is_superuser = False
        user.is_active = True
        user.set_password('123')
        user.save()

    # создаем модератора блогов
        user = User.objects.create(
            email='blogs_moderator@ysky.pro',
            first_name='Blogs',
            last_name='Moderator',
        )
        user.is_staff = True
        user.is_superuser = False
        user.is_active = True
        user.set_password('123')
        user.save()