from django.db import models
from django.contrib.auth.models import User

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
    
class Scope(models.Model):
    hum_min = models.FloatField(default=15)
    hum_max = models.FloatField(default=100, max_length=100)
    temp_min = models.FloatField(default=5)
    temp_max = models.FloatField(default=60, max_length=100)
    idUser = models.ForeignKey(User)
    
    def __unicode__(self):
        return str(self.idUser)