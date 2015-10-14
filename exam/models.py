
from django.db import models



class problem(models.Model):
    name = models.CharField(max_length=50)
    accessType = models.ManyToManyField('group')
    owner = models.ForeignKey('user')
    price = models.IntegerField(default=0)
    text = models.CharField(max_length=5000)
    answer = models.CharField(max_length=50)
    isShortAnswer = models.BooleanField(default=0)
    usesFormula = models.BooleanField(default=0)
    formula = models.CharField(max_length=500)

    def __unicode__(self):
        return self.name


class bundle(models.Model):
    name = models.CharField(max_length=50)
    owner = models.ForeignKey('user')
    problems = models.ManyToManyField('problem')
    price = models.IntegerField(default=0)

    def __unicode__(self):
        return self.name


class exam(models.Model):
    name = models.CharField(max_length=50)
    startDate = models.DateTimeField()
    endDate = models.DateTimeField()
    problems = models.ManyToManyField('problem')
    owner = models.ForeignKey('user', related_name="owner")
    price = models.IntegerField(default=0)
    participant = models.ManyToManyField('user', related_name="participant")
    public = models.BooleanField(default=0)



class problem(models.Model):
    name = models.CharField(max_length=50)
    accessType = models.ManyToManyField('group')
    owner = models.ForeignKey('user')
    price = models.IntegerField(default=0)
    text = models.CharField(max_length=5000)
    answer = models.CharField(max_length=50)
    isShortAnswer = models.BooleanField(default=0)
    usesFormula = models.BooleanField(default=0)
    formula = models.CharField(max_length=500)



