import json
from django.shortcuts import render_to_response, render
from django.template import RequestContext
from measurement.models import MeasurementData, Sensor, Scope
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from measurement.forms import ScopeForm
from mailing.views import threadmethod
from django.http import HttpResponseRedirect

#metoda do wysywania maili
threadmethod()

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



def create_scope(request, sensorr):
    form = ScopeForm(request.POST or None)
    user = request.user
    if form.is_valid():
        save_it = form.save(commit=False)
        save_it.idUser = user
        save_it.sensor = sensorr
        save_it.save()
    

#TODO uztkownik moze tylko raz zapisac wskaznik do danego czujnika
def scope(request):
    tempMax = None
    tempMin = None
    humMax = None
    humMin = None
    state = None
    all_sensor = Sensor.objects.all()
    if request.POST:
        user = request.user
        sensorPOST = request.POST.get('s', False)
        sensorId = Sensor.objects.get(nameSensor = sensorPOST)
        users_scope = Scope.objects.filter(idUser = user.id, sensor = sensorId).values()
        if (users_scope):
            state = True
            tempMax = users_scope[0]['temp_max']
            tempMin = users_scope[0]['temp_min']
            humMax = users_scope[0]['hum_max']
            humMin = users_scope[0]['hum_min']
        else:
            print sensorId.id
            sensorr = sensorId.id
            create_scope(request, sensorr);
    return render_to_response('scope.html',  {'state':state, 'form': ScopeForm(),
                                               'sensor': all_sensor, 'temp_min': tempMin, 'temp_max': tempMax, 'hum_max':humMax, 'hum_min':humMin }, context_instance=RequestContext(request))

