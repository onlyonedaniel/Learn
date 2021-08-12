from django.db import models

# Create your models here.


class LatestData(models.Model):
    array = models.CharField(max_length=2000)


class Data(models.Model):
    array = models.CharField(max_length=2000)
