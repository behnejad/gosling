# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_User'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reset',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('hash_code', models.CharField(max_length=30)),
                ('time_request', models.DateTimeField(default=django.utils.timezone.now)),
                ('user', models.ForeignKey(to='user.User')),
            ],
        ),
    ]
