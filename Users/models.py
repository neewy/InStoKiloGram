from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    type_choices = (
        ('SU', 'Super User'),
        ('A', 'General User'),
        ('B', 'Dietitian'),
        ('C', 'Fitness Trainer'),
    )

    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    nickname = models.CharField(max_length=100)
    dateOfBirth = models.CharField(max_length=100)

    user_type = models.CharField(max_length=2,
                                 choices=type_choices,
                                 default='A')

class UserProfile(models.Model):
    gender_choices = (
        ('M', 'Male'),
        ('F', 'Female'),
    )

    gender = models.CharField(max_length=1,
                              choices=gender_choices
                              )

    start_weight = models.DecimalField(max_digits=3,
                                       decimal_places=2
                                       )