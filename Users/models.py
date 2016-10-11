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
    activity_choices = (
        ('S', 'Sedentary'),
        ('LA', 'Low active'),
        ('A', 'Active'),
        ('VA', 'Very active'),
    )
    goals_choices = (
        ('MWG', 'Moderate weight gain'),
        ('GWG', 'Gradual weight gain'),
        ('MCW', 'Maintain current weight'),
        ('GWL', 'Gradual weight loss'),
        ('MWL', 'Moderate weight loss'),
    )

    gender = models.CharField(max_length=1,
                              choices=gender_choices
                              )

    start_weight = models.DecimalField(max_digits=3,
                                       decimal_places=2
                                       )
    current_weight = models.DecimalField(max_digits=3,
                                         decimal_places=2,
                                         default=start_weight
                                         )
    goal_weight = models.DecimalField(max_digits=3,
                                      decimal_places=2,
                                      )
    height = models.DecimalField(max_digits=3,
                                 decimal_places=2,
                                 )
    birth_date = models.DateField

    activity_level = models.CharField(max_length=2,
                                      choices=activity_choices
                                      )
    diet_goals = models.CharField(max_length=100,
                                  choices=goals_choices
                                  )
