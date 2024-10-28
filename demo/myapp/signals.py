# signals.py
from django.db.models.signals import post_migrate
from django.contrib.auth.models import Group, Permission
from django.dispatch import receiver
from django.apps import AppConfig


@receiver(post_migrate)
def create_user_types(sender, **kwargs):
    if sender.name == 'myapp':  # replace with your app name
        # Create groups
        # artists, _ = Group.objects.get_or_create(name='Artists')
        artists, _ = Group.objects.get_or_create(name='Artist')
        admins, _ = Group.objects.get_or_create(name='Admins')

        # Assign permissions
        view_permission = Permission.objects.get(codename='view_svgimage')
        change_permission = Permission.objects.get(codename='change_svgimage')
        delete_permission = Permission.objects.get(codename='delete_svgimage')

        artists.permissions.add(view_permission, change_permission, delete_permission)
        admins.permissions.set(Permission.objects.all())
