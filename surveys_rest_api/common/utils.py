from django.core.exceptions import ImproperlyConfigured
from django.contrib.auth.models import Permission


def add_permission(permission=None, user=None):
    """
        Add a new permission to the user passed as parameter
    """
    if user and permission:
        permission = Permission.objects.get(name='Can {0}'.format(permission))
        user.user_permissions.add(permission)


def check_fields(fields=None):
    """
        Check that all the fields needed in a mixin have been set up properly
    """
    for field in fields:
        if not fields[field]:
            raise ImproperlyConfigured(
                '"{0}" field must be defined'.format(field)
            )
