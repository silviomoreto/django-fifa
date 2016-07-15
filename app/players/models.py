# coding: utf-8
from django.contrib.auth.models import User
from django.db import models


class Player(models.Model):
    # user = models.OneToOneField(User, verbose_name=u'user')
    name = models.CharField(u'player name', max_length=255)
    email = models.EmailField(u'e-mail', blank=True, null=True)
    ranking = models.IntegerField(u'ranking', default=1200)
    victories = models.IntegerField(u'vicotories', default=0)
    draws = models.IntegerField(u'draws', default=0)
    losses = models.IntegerField(u'losses', default=0)

    class Meta:
        verbose_name, verbose_name_plural = 'player', 'players'

    def __unicode__(self):
        return self.name


class Team(models.Model):
    name = models.CharField(u'Team Name', max_length=128)
    country = models.CharField(u'Team country', max_length=128, blank=True, null=True)

    class Meta:
        verbose_name, verbose_name_plural = 'team', 'teams'

    def __unicode__(self):
        return self.name
