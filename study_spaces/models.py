# https://www.w3schools.com/python/ref_string_format.asp
from django.db import models


class StudySpace(models.Model):
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    latitude = models.FloatField(default=0.0)
    longitude = models.FloatField(default=0.0)
    approved_submission = models.BooleanField(default=False)

    def get_sentence(self):
        return "{name} is located at {address}.".format(name=self.name, address=self.address)

    def __str__(self):
        return self.name