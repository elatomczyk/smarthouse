import json
from django.shortcuts import render_to_response, render
from django.template import RequestContext
from measurement.models import MeasurementData, Sensor
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from measurement.forms import ScopeForm


def index(request):
    sensor = Sensor.objects.all()
    data = []
    for s in sensor:
        m = MeasurementData.objects.filter(idSensor=s).order_by('timestamp').last()
        if m:
            data.append(m)

    return render_to_response('index.html', {'data': data}, context_instance=RequestContext(request))


@login_required
def user_account(request):
    return render(request,'account.html')


def user_home(request):
    return render(request, 'home.html')

#metoda ta zapisuje dane uzyskane od czujnika do bazy
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

def create_scope(request):
    form = ScopeForm(request.POST or None)
    user = request.user
    all_sensor = Sensor.objects.all()
    if form.is_valid():
        save_it = form.save(commit=False)
        save_it.idUser = user
        save_it.save()
    return render_to_response('scope.html', locals(), context_instance=RequestContext(request))
'''    
def scope(request): 
    all_sensor = Sensor.objects.all() 
    if request.POST: 
        choice = Sensor.objects.filter(id=request.POST.get('choice', False)) 
    else: 
        choice = 0 
    return render_to_response('scope.html', {'all_sensor': all_sensor}, context_instance=RequestContext(request)) 
'''
