from django.core.management import BaseCommand
from users.models import User

class Command(BaseCommand):
    """Команда создания суперюзера"""

    def handle(self, *args, **options):
       user = User.objects.create(
            email='admin@skystore.pro',
            first_name='Admin',
            last_name='Skystore',
        )
       user.is_staff = True
       user.is_superuser = True
       user.is_active = True
       user.set_password('123')
       user.save()