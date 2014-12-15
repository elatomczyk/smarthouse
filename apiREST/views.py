from django.shortcuts import render
from measurement.models import MeasurementData
from apiREST.serializers import MeasurementDataSerializer
from rest_framework.response import Response
from rest_framework.views import APIView

# Create your views here.
class MeasurementDataREST(APIView):
    def get(self, request, format=None):
        serializer_Measurement = MeasurementDataSerializer(MeasurementData.objects.order_by('timestamp').last())
        return Response(serializer_Measurement.data)