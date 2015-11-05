# -*- coding: utf-8 -*-

from django.db import models
from user.hashmanager import makeHash
from datetime import datetime


class mail(models.Model):
    email = models.CharField(max_length=50)
    hashId = models.CharField(max_length=50)


class User(models.Model):
    mode = ((False, 'No'), (True, 'Yes'))
    mode2 = (('T', 'Teacher'), ('S', 'Student'), ('O', 'Free User'))

    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    password = models.CharField(max_length=60, help_text='This is not real')
    email = models.EmailField(max_length=50)
    date_create = models.DateTimeField()
    is_activate = models.BooleanField(default=False, choices=mode)
    type = models.CharField(max_length=1, choices=mode2, default='S')
    request = models.BooleanField(default=False, choices=mode)
    ban = models.BooleanField(default=False, choices=mode)

    def __unicode__(self):
        return ' '.join((self.first_name, self.last_name))

    def is_valid_pass(self, pwd, password):
        return makeHash(pwd, password.encode("utf8"), self.email.encode("utf8")) == self.password

    @property
    def person(self):
        return ' '.join((self.first_name, self.last_name))

    @property
    def key(self):
        return makeHash(self.password, self.email)


class Reset(models.Model):
    hash_code = models.CharField(max_length=30)
    time_request = models.DateTimeField(default=datetime.now())
    user = models.ForeignKey("User")

    def __str__(self):
        return self.hash_code

    def __unicode__(self):
        return self.hash_code


class group(models.Model):
    name = models.CharField(max_length=50)
    admin = models.ForeignKey(User)


class prereg(models.Model):
    mail = models.CharField(max_length=30)
    smash = models.CharField(max_length=50)

