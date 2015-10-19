# -*- coding: utf-8 -*-

from django.db import models
from hashmanager import HashManager

class mail(models.Model):
    email = models.CharField(max_length=50)
    hashId = models.CharField(max_length=50)


class User(models.Model):
    mode = ((False, 'No'), (True, 'Yes'))
    mode2 = (('T', 'Teacher'), ('S', 'Student'), ('O', 'Free User'))

    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    username = models.CharField(max_length=30, db_index=True)
    password = models.CharField(max_length=60, help_text='This is not real')
    email = models.EmailField(max_length=50)
    datecreate = models.DateTimeField()
    isactivate = models.BooleanField(default=False, choices=mode)
    type = models.CharField(max_length=1, choices=mode2, default='S')
    request = models.BooleanField(default=False, choices=mode)
    ban = models.BooleanField(default=False, choices=mode)

    def __unicode__(self):
        return ' '.join((self.first_name, self.last_name))

    def isValidPass(self, pwd=''):
        hash = HashManager()
        return hash.makeHash(pwd, self.username) == self.password

    @property
    def person(self):
        return ' '.join((self.first_name, self.last_name))

    @property
    def key(self):
        hash = HashManager()
        return hash.makeHash(self.username, self.password, self.email)



class group(models.Model):
    name = models.CharField(max_length=50)
    admin = models.ForeignKey(User)

