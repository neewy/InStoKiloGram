from __future__ import unicode_literals

import datetime
from django.db import models
from django.utils.translation import gettext
from django.db.models.manager import Manager


class PublishedManager(Manager):
    def get_query_set(self):
        return super(PublishedManager, self).get_query_set().filter(is_published=True)


class Poll(models.Model):
    title = models.CharField(max_length=250, verbose_name=gettext('question'))
    date = models.DateField(verbose_name=gettext('date'), default=datetime.date.today)
    is_published = models.BooleanField(default=True, verbose_name=gettext('is published'))

    objects = models.Manager()
    published = PublishedManager()

    class Meta:
        ordering = ['-date']
        verbose_name = gettext('poll')
        verbose_name_plural = gettext('polls')

    def __unicode__(self):
        return self.title

    def get_vote_count(self):
        return Vote.objects.filter(poll=self).count()

    vote_count = property(fget=get_vote_count)

    def get_cookie_name(self):
        return str('poll_%s' % self.pk)


class Item(models.Model):
    poll = models.ForeignKey(Poll)
    value = models.CharField(max_length=250, verbose_name=gettext('value'))
    pos = models.SmallIntegerField(default='0', verbose_name=gettext('position'))

    class Meta:
        verbose_name = gettext('answer')
        verbose_name_plural = gettext('answers')
        ordering = ['pos']

    def __unicode__(self):
        return u'%s' % (self.value,)

    def get_vote_count(self):
        return Vote.objects.filter(item=self).count()

    vote_count = property(fget=get_vote_count)


class Vote(models.Model):
    poll = models.ForeignKey(Poll, verbose_name=gettext('poll'))
    item = models.ForeignKey(Item, verbose_name=gettext('voted item'))
    user = models.ForeignKey('Users.User', blank=True, null=True,
                             verbose_name=gettext('user'))
    datetime = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = gettext('vote')
        verbose_name_plural = gettext('votes')
