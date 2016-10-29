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

    vkid = models.BigIntegerField( default = 0 )
    photourl = models.CharField(max_length=500, default="")
    #
    # photoimage = models.ImageField(upload_to='/media/avatar', null=True, blank=True)


    gender_choices = (
        ('M', 'Male'),
        ('F', 'Female'),
        # ('U', 'Undefined'),
    )
    activity_choices = (
        ('S', 'Sedentary'),
        ('LA', 'Low active'),
        ('A', 'Active'),
        ('VA', 'Very active'),
        # ('U', 'Undefined'),
    )
    goals_choices = (
        ('MWG', 'Moderate weight gain'),
        ('GWG', 'Gradual weight gain'),
        ('MCW', 'Maintain current weight'),
        ('GWL', 'Gradual weight loss'),
        ('MWL', 'Moderate weight loss'),
        # ('U', 'Undefined'),
    )

    gender = models.CharField(max_length=1,
                              choices=gender_choices,
                              default='U'
                              )

    start_weight = models.FloatField(default=0)

    current_weight = models.FloatField(default=0)

    goal_weight = models.FloatField(default=0)

    height = models.FloatField(default=0)

    activity_level = models.CharField(max_length=2,
                                      choices=activity_choices,
                                      default='U'
                                      )
    birth_date = models.DateField(default='1888-01-01')

    diet_goals = models.CharField(max_length=100,
                                  choices=goals_choices,
                                  default='U'
                                  )
