#!coding=utf-8

from django.db import models

class Poll(models.Model):
    question = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __unicode__(self):
         return self.question


class Choice(models.Model):
    poll = models.ForeignKey(Poll)  #自动对应poll模型的关键字
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    def __unicode__(self):
         return self.choice_text
