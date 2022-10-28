from django.core.management.base import BaseCommand
from django.contrib.auth.models import User

password = 'test123'


class Command(BaseCommand):
    def handle(self, *args, **options):
        if User.objects.count() == 0:
            user = User.objects.create_user('test_admin', password=password)
            user.is_superuser = True
            user.is_staff = True
            user.save()
            return "User 'test_admin' created successfully."
