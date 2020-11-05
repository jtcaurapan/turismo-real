from django.db import models

class Apartment(models.Model):
    name = models.CharField(max_length=15)
    description = models.CharField(max_length=255)
    rate = models.IntegerField()
    capacity = models.IntegerField()
