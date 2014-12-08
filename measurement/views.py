import json
from django.shortcuts import render_to_response
from django.template import RequestContext
from measurement.models import MeasurementData
from django.http import JsonResponse


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
    data = MeasurementData.objects.all()
    return render_to_response('diagram.html', {'data': data}, context_instance=RequestContext(request))