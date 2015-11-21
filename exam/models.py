from django.db import models
from user.models import group, User


class period(models.Model):
    name = models.CharField(max_length=40)

    def __unicode__(self):
        return self.name


class field(models.Model):
    name = models.CharField(max_length=40)

    def __unicode__(self):
        return self.name



class section(models.Model):
    name = models.CharField(max_length=40)

    def __unicode__(self):
        return self.name


class problem(models.Model):
    # course = models.ForeignKey(field)
    # term = models.ForeignKey(period)
    # sec = models.ForeignKey(section)
    text = models.TextField()
    answers = models.TextField()


    # def __unicode__(self):
    #     return ' - '.join((self.coursode__(self):
    #     return ' - '.join((self.course, self.term, self.sec))



