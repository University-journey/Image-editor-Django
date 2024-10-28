from django.db.models.signals import post_migrate

# def create_user_types(sender, **kwargs):
#     from django.contrib.auth.models import Group, Permission
#
#     # Create groups
#     ordinary_users, created = Group.objects.get_or_create(name='Ordinary Users')
#     artists, created = Group.objects.get_or_create(name='Artists')
#     admins, created = Group.objects.get_or_create(name='Admins')
#
#     # Assign permissions
#     # For simplicity, using Django's built-in permissions
#     # Ordinary Users - Can view images
#     ordinary_users.permissions.set(Permission.objects.filter(codename__in=['view_image']))
#
#     # Artists - Can view and change images
#     artists.permissions.set(Permission.objects.filter(codename__in=['view_image', 'change_image']))
#
#     # Admins - Can do anything including accessing the admin panel
#     admins.permissions.set(Permission.objects.all())

# myapp/apps.py
from django.apps import AppConfig

class MyappConfig(AppConfig):
    name = 'myapp'
    default_auto_field = 'django.db.models.BigAutoField'

    def ready(self):
        from . import signals  # This line imports the signals module, connecting the signals