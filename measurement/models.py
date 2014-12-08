from django.db import models

# Create your models here.
class MeasurementData(models.Model):
    timestamp = models.DateTimeField()
    temperature = models.FloatField(default=-100.)
    humidity = models.FloatField(default=-100.)