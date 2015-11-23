from django.db import models
from user.models import group, User


class field(models.Model):
    name = models.CharField(max_length=40)

    def __unicode__(self):
        return self.name


class section(models.Model):
    fname = models.ForeignKey(field)
    name = models.CharField(max_length=40)

    def __unicode__(self):
        return self.fname.name + ' - ' + self.name


class problem(models.Model):
    sec = models.ForeignKey(section)
    text = models.TextField()
    question = models.TextField()
    answers = models.TextField()


    # def __unicode__(self):
    #     return ' - '.join((self.coursode__(self):
    #     return ' - '.join((self.course, self.term, self.sec))



