from django.db import models


class Rating(models.Model):
    rating = models.IntegerField()
    restaurant = models.UUIDField()
