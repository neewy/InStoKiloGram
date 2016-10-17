from __future__ import unicode_literals

import pretty
from django.db import models
from django.utils import timezone

class Post(models.Model):
    author = models.ForeignKey('Users.User')
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
    image = models.ImageField(upload_to='pic_folder/', blank=True)
    tags = models.ManyToManyField('Tag')

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def get_pretty_date(self):
        time = timezone.make_naive(self.published_date)
        return pretty.date(time, short=True)

    def __str__(self):
        return self.title


class Tag(models.Model):
    tag_name = models.CharField(max_length=20)
    tag_url = models.URLField(null=True, blank=True)

    def __str__(self):
        return self.tag_name