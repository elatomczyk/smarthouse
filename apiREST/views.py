from reportlab.graphics.widgetbase import Face
from django.contrib.auth.models import User
from rest_framework.decorators import api_view
from measurement.models import MeasurementData, Sensor, Scope
from apiREST.serializers import MeasurementDataSerializer, SensorSerializer
from rest_framework.response import Response
from rest_framework.views import APIView


class MeasurementDataREST(APIView):
    def get(self, request, format=None):
        serializer_Measurement = MeasurementDataSerializer(MeasurementData.objects.order_by('timestamp').last())
        return Response(serializer_Measurement.data)


class MeasurementGraphREST(APIView):
    def get(self, request, limit, format=None):
        dataGraph = MeasurementDataSerializer(MeasurementData.objects.order_by('-timestamp')[:limit], many=True)
        return Response(dataGraph.data)


class SensorREST(APIView):
    def get(self, request, format=None):
        list = Sensor.objects.all()
        dataSensor = SensorSerializer(list, many=True)
        return Response(dataSensor.data)

@api_view(['POST'])
def login(request):
    #Django REST metoda logowania
    if request.method == 'POST':
        try:
           user = User.objects.get(username=request.POST.get('username'))
        except User.DoesNotExist:
            return Response({"information": "Problem with username"})

        if user.check_password(request.POST.get('password')):
            return Response({"information": "Logged"})
        else:
            return Response({"information": "Problem with password"})
    return Response({"information": "Problem with program"})


class CheckScope(APIView):
    def get(self, request, username, format=None):
        user = User.objects.get(username=username)
        scope = Scope.objects.filter(idUser=user).values()

        tab = []
        addingDouble = False
        for s in scope:
            measurement = MeasurementData.objects.filter(idSensor=s['sensor_id']).order_by('-timestamp').values().last()

            if not measurement:
                break

            sensor = Sensor.objects.get(id=measurement['idSensor_id'])

            if measurement['temperature'] > s['temp_max'] or measurement['temperature'] < s['temp_min']:
                tab.append(createData(True, sensor.nameSensor, measurement['temperature'], measurement['humidity']))
                addingDouble = True

            if measurement['humidity'] > s['hum_max'] or s['hum_min'] > measurement['humidity']:
                if addingDouble == False:
                    tab.append(createData(True, sensor.nameSensor, measurement['temperature'], measurement['humidity']))

            addingDouble = False

        if not tab:
            tab.append(createData(False, 0, 0, 0))

        return Response(tab)


def createData(scope,sensor,temperature,humidity):
    data = {'scope': scope,
        'sensor': sensor,
        'temperature': temperature,
        'humidity': humidity,
        }
    return data