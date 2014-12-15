from measurement.models import MeasurementData
from django.contrib.auth.models import User

from rest_framework import serializers

class MeasurementDataSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = MeasurementData
        fields = ('timestamp', 'temperature', 'humidity',)
