from django.db import models


class StudySpace(models.Model):
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    latitude = models.FloatField
    longitude = models.FloatField
