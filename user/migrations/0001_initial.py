# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='group',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=1000)),
                ('date_created', models.DateTimeField()),
                ('is_activate', models.BooleanField(default=True, choices=[(False, b'No'), (True, b'Yes')])),
                ('password', models.CharField(help_text=b'This is not real', max_length=60)),
            ],
        ),
        migrations.CreateModel(
            name='group_user_relation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('type', models.CharField(default=b'T', max_length=1, choices=[(b'T', b'Teacher'), (b'S', b'Student')])),
                ('group', models.ForeignKey(to='user.group')),
            ],
        ),
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
            name='Reset',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('hash_code', models.CharField(max_length=30)),
                ('time_request', models.DateTimeField(default=django.utils.timezone.now)),
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
        migrations.AddField(
            model_name='reset',
            name='user',
            field=models.ForeignKey(to='user.User'),
        ),
        migrations.AddField(
            model_name='group_user_relation',
            name='user',
            field=models.ForeignKey(to='user.User'),
        ),
        migrations.AddField(
            model_name='group',
            name='admin',
            field=models.ForeignKey(to='user.User'),
        ),
    ]
