from django.db import models


class Movie(models.Model):
    title = models.CharField(max_length=250)
    year = models.IntegerField()
    poster = models.CharField(max_length=1000)
