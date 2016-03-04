from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _
import uuid
import os

# Create your models here.


def get_file_path(instance, filename):
    file_extension = filename.split('.')[-1]
    filename = "{file_name}.{file_extension}".format(
        file_name=uuid.uuid4(), file_extension=file_extension
    )
    path = os.path.join('accounts/user_profile', filename)
    return path


class UserProfile(AbstractUser):

    class Meta:
        verbose_name = _('User')
        verbose_name_plural = _('Users')

    GENDER_CHOICES = [
        ('Male', _('Male')),
        ('Female', _('Female'))
    ]

    birthday = models.DateField(null=True, blank=True)
    gender = models.CharField(
        _('User gender'),
        max_length=6,
        choices=GENDER_CHOICES,
        blank=True,
        help_text=_('Select a gender for the user profile')
    )
    id_network = models.CharField(blank=True, max_length=100)
    biography = models.TextField(blank=True, max_length=300)
    updated_at = models.DateTimeField(auto_now=True)
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
            first_name=self.first_name,
            last_name=self.last_name)
