# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import accounts.models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('age', models.PositiveSmallIntegerField(help_text='Write an age for the user profile', null=True, verbose_name='User age', blank=True)),
                ('gender', models.CharField(blank=True, help_text='Select a gender for the user profile', max_length=6, verbose_name='User gender', choices=[(b'Male', 'Male'), (b'Female', 'Female')])),
                ('image_profile', models.ImageField(default=b'/static/accounts/img/profile-photo.png', upload_to=accounts.models.get_file_path, blank=True, help_text='Upload an image for the user profile', verbose_name='User image profile')),
                ('authentication_user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'User',
                'verbose_name_plural': 'Users',
            },
            bases=(models.Model,),
        ),
    ]
