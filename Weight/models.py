from django.db import models

class Weight(models.Model):
    date = models.DateTimeField()
    user_id = models.IntegerField()
    weight = models.FloatField()

class FoodDiary(models.Model):
    mealtime_choices = (
        ('Breakfast', 'Breakfast'),
        ('Lunch', 'Lunch'),
        ('Dinner', 'Dinner'),
        ('Snacks', 'Snacks/Other'),
    )
    user_id = models.IntegerField()
    date = models.DateField()
    food = models.CharField(max_length=200)
    mealtime = models.CharField(max_length=100, choices=mealtime_choices)
    calories = models.FloatField(default=0)
    fat = models.FloatField(default=0)
    carbs = models.FloatField(default=0)
    prot = models.FloatField(default=0)
