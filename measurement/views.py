import json
from django.shortcuts import render_to_response
from django.template import RequestContext
from measurement.models import MeasurementData, Sensor
from django.http import JsonResponse
#  $('.dateinput').datepicker({ format: "yyyy/mm/dd" });

def index(request):
    data = MeasurementData.objects.order_by('timestamp').last()
    return render_to_response('index.html', {'data': data}, context_instance=RequestContext(request))


# metoda ta zapisuje dane uzyskane od czujnika do bazy
def measurement(request):
    print str(request.method)
    data_json = json.loads(request.body)
    m = MeasurementData(timestamp=data_json['timestamp'],
                        temperature=data_json['temperature'],
                        humidity=data_json['humidity'])
    m.save()

    return JsonResponse({'status': 'ok'})


def diagram(request):
    if request.POST:
        sensorPOST = request.POST.get('s', False)
        sensorId = Sensor.objects.get(nameSensor=sensorPOST)
        date_start = request.POST.get('dateStart', False)
        date_end = request.POST.get('dateEnd', False)

        data = MeasurementData.objects.filter(idSensor=sensorId, timestamp__gte=date_start, timestamp__lte=date_end)
        text = "----"
    else:
        text = "Wszystkie Pomiary"
        data = MeasurementData.objects.all()

    sensor = Sensor.objects.all()

    return render_to_response('diagram.html', {'data': data, 'sensor': sensor, 'text':text}, context_instance=RequestContext(request))


