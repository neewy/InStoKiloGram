from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Food(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    calories = models.IntegerField()

    def publish(self):
        self.save()

    def __str__(self):
        return self.name