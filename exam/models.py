from django.db import models
from user.models import group, User
from datetime import datetime

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
    correctanswer = models.IntegerField()
    
    def anss(self):
        return self.answers.split('|')[:-1]

    def __unicode__(self):
        return self.sec.__unicode__()

        
class exam(models.Model):
    groupid = models.ForeignKey(group)
    startdate = models.DateTimeField()
    enddate = models.DateTimeField()
    name = models.CharField(max_length=80)

    def __unicode__(self):
        return self.name

    @property
    def isStart(self):
        return self.startdate < datetime.now() < self.enddate


class examproblems(models.Model):
    examid = models.ForeignKey(exam)
    problemid = models.ForeignKey(problem)


class useranswers(models.Model):
    examid = models.ForeignKey(exam)
    problemid = models.ForeignKey(problem)
    userid = models.ForeignKey(User)
    answer = models.IntegerField(default=0)
