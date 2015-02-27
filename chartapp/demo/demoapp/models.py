from django.db import models


class LineModel (models.Model):
    xfield = models.IntegerField(default=0)
    yfield = models.IntegerField(default=0)


class DonutModel(models.Model):
    label = models.CharField(max_length=50)
    value = models.IntegerField(default=0)
    color = models.CharField(blank=True, max_length=50)
