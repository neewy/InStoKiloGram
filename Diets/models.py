from __future__ import unicode_literals

import pretty
from django.db import models
from django.utils import timezone


class Diet(models.Model):
    name = models.CharField(max_length=40)
    author = models.ForeignKey('Users.User', blank=True, null=True)
    text = models.TextField()
    recipes = models.ManyToManyField('Recipes.Recipe', blank=True)
    created_date = models.DateTimeField(default=timezone.now)
    image = models.ImageField(upload_to='pic_folder/', blank=True)
    published_date = models.DateTimeField(blank=True, null=True)

    def get_pretty_date(self):
        time = timezone.make_naive(self.published_date)
        return pretty.date(time, short=True)

    def get_score(self):
        scores = DietReview.objects.filter(diet=self)
        avg = 0.0
        for score in scores:
            avg += score.rating
        if not scores:
            return "?"
        else:
            avg /= len(scores)
            return avg

    def __str__(self):
        return self.name


class DietReview(models.Model):
    RATING_CHOICES = (
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
    )
    title = models.CharField(max_length=20)
    author = models.ForeignKey('Users.User')
    diet = models.ForeignKey('Diets.Diet')
    pub_date = models.DateTimeField('Date Published')
    rating = models.IntegerField(choices=RATING_CHOICES)
    review_text = models.TextField()

    def sort_reviews_avg(self, review2):
        if self.rating > review2.rating:
            return 1
        elif review2.rating > self.rating:
            return -1
        else:
            return 0

    def get_pretty_date(self):
        time = timezone.make_naive(self.pub_date)
        return pretty.date(time, short=True)

    def __str__(self):
        return self.title
