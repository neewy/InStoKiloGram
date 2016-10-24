from django.db import models

class Weight(models.Model):
    date = models.DateTimeField()
    user_id = models.IntegerField()
    weight = models.FloatField()