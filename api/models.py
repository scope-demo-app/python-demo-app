from django.db import models


class Restaurant(models.Model):
    name= models.CharField(max_length=30)
    description= models.CharField(max_length=300)
