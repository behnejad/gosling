# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_reset'),
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
                ('admin', models.ForeignKey(to='user.User')),
            ],
        ),
        migrations.CreateModel(
            name='group_user_relation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('type', models.CharField(default=b'T', max_length=1, choices=[(b'T', b'Teacher'), (b'S', b'Student')])),
                ('group', models.ForeignKey(to='user.group')),
                ('user', models.ForeignKey(to='user.User')),
            ],
        ),
    ]
