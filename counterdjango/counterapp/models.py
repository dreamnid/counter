from django.db import models

# Create your models here.


class Counter(models.Model):
    name = models.CharField(blank=True, max_length=16, null=False)
    count = models.IntegerField()


class MySQLCounter(models.Model):
    name = models.CharField(blank=True, max_length=16, null=False)
    count = models.IntegerField()
