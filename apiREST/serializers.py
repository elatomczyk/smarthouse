from measurement.models import MeasurementData, Sensor, Rooms


from rest_framework import serializers


class SensorSerializer(serializers.ModelSerializer):
    idRoom = serializers.StringRelatedField()
    class Meta:
        model = Sensor
        fields = ('id', 'nameSensor', 'idRoom')



class MeasurementDataSerializer(serializers.ModelSerializer):
    timestamp = serializers.DateTimeField(format='%Y-%m-%d, %H:%m')
    idSensor = SensorSerializer()

    class Meta:
        model = MeasurementData
        fields = ('idSensor', 'timestamp', 'temperature', 'humidity',)


