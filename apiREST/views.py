from django.contrib.auth.models import User
from rest_framework.decorators import api_view
from measurement.models import MeasurementData
from apiREST.serializers import MeasurementDataSerializer
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

