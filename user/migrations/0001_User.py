# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='mail',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('email', models.CharField(max_length=50)),
                ('hashId', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='prereg',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('mail', models.CharField(max_length=30)),
                ('smash', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('password', models.CharField(help_text=b'This is not real', max_length=60)),
                ('email', models.EmailField(max_length=50)),
                ('date_create', models.DateTimeField()),
                ('is_activate', models.BooleanField(default=False, choices=[(False, b'No'), (True, b'Yes')])),
                ('type', models.CharField(default=b'S', max_length=1, choices=[(b'T', b'Teacher'), (b'S', b'Student'), (b'O', b'Free User')])),
                ('request', models.BooleanField(default=False, choices=[(False, b'No'), (True, b'Yes')])),
                ('ban', models.BooleanField(default=False, choices=[(False, b'No'), (True, b'Yes')])),
            ],
        ),
    ]
