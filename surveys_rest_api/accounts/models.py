from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _
import uuid
import os

# Create your models here.


def get_file_path(instance, filename):
    """
    Helper function to provide user profile images an unique filename
    to avoid overwrites
    """
    file_extension = filename.split('.')[-1]
    filename = "{file_name}.{file_extension}".format(
        file_name=uuid.uuid4(), file_extension=file_extension
    )
    path = os.path.join('accounts/user_profile', filename)
    return path


class UserProfile(models.Model):
    """
        Model to handle user profile information and extend
        the functionality of the basic Django User model and its fields
    """

    class Meta:
        verbose_name = _('User')
        verbose_name_plural = _('Users')

    GENDER_CHOICES = [
        ('Male', _('Male')),
        ('Female', _('Female'))
    ]

    authentication_user = models.OneToOneField(User)
    age = models.PositiveSmallIntegerField(
        _('User age'),
        null=True,
        blank=True,
        help_text=_('Write an age for the user profile')
    )
    gender = models.CharField(
        _('User gender'),
        max_length=6,
        choices=GENDER_CHOICES,
        blank=True,
        help_text=_('Select a gender for the user profile')
    )
    image_profile = models.ImageField(
        _('User image profile'),
        blank=True,
        upload_to=get_file_path,
        default='{url}{image_path}'.format(
            url=settings.STATIC_URL,
            image_path='accounts/img/profile-photo.png'
        ),
        help_text=_('Upload an image for the user profile')
    )

    def __unicode__(self):
        return '{first_name} {last_name}'.format(
            first_name=self.authentication_user.first_name,
            last_name=self.authentication_user.last_name)
