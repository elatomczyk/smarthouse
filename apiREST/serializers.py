from measurement.models import MeasurementData, Sensor, Rooms


from rest_framework import serializers


class SensorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sensor
        fields = ('id', 'nameSensor',)



class MeasurementDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = MeasurementData
        fields = ('idSensor', 'timestamp', 'temperature', 'humidity',)


