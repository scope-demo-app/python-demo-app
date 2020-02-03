from django.db import models


class Rating(models.Model):
    STAR_1 = '1'
    STAR_2 = '2'
    STAR_3 = '3'
    STAR_4 = '4'
    STAR_5 = '5'
    RATING_CHOICES = [
        (STAR_1, '1 star'),
        (STAR_2, '2 stars'),
        (STAR_3, '3 stars'),
        (STAR_4, '4 stars'),
        (STAR_5, '5 stars'),
    ]
    rating = models.CharField(max_length=1, choices= RATING_CHOICES)
    restaurant = models.UUIDField()
