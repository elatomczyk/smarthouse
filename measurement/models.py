from django.db import models

# Create your models here.

class Rooms(models.Model):
    nameRoom = models.CharField(max_length=100)

    def __unicode__(self):
        return str(self.nameRoom)

class Sensor(models.Model):
    nameSensor = models.CharField(max_length=100)
    idRoom = models.ForeignKey(Rooms)

    def __unicode__(self):
        return str(self.nameSensor)

class MeasurementData(models.Model):
    timestamp = models.DateTimeField()
    temperature = models.FloatField(default=-100.)
    humidity = models.FloatField(default=-100.)
    idSensor = models.ForeignKey(Sensor)

    def __unicode__(self):
        return str(self.temperature)