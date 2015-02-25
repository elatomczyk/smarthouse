import json
from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist, ValidationError
from django.shortcuts import render_to_response, render
from django.template import RequestContext
from measurement.models import MeasurementData, Sensor, Scope
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from measurement.forms import ScopeForm
from mailing.views import threadmethod
from django.http import HttpResponseRedirect

#metoda do wysywania maili
#threadmethod()

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
    return render(request, 'account.html')


def custom_login(request):
    if request.user.is_authenticated():
        return HttpResponseRedirect("/")
    else:
        return login(request)


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
    sensor = Sensor.objects.all()
    try:
        if request.POST:
            sensorPOST = request.POST.get('s', False)
            sensorId = Sensor.objects.get(nameSensor=sensorPOST)
            date_start = request.POST.get('dateStart', False)
            date_end = request.POST.get('dateEnd', False)

            data = MeasurementData.objects.filter(idSensor=sensorId, timestamp__gte=date_start, timestamp__lte=date_end)
            text = "----"
        else:
            text = "Wszystkie Pomiary"
            data = MeasurementData.objects.filter(idSensor=1)
            sensor = Sensor.objects.all()

        sensor = Sensor.objects.all()
    except ObjectDoesNotExist:
        textproblem = "Prosze o wybranie czujnika."
        return render(request, 'diagram.html', { 'problem': textproblem, 'sensor': sensor })
    except ValidationError as e:
        textproblem = "Prosze o wybranie daty."
        return render(request, 'diagram.html', { 'problem': textproblem, 'sensor': sensor})
    return render_to_response('diagram.html', {'data': data, 'sensor': sensor, 'text': text}, context_instance=RequestContext(request))



def create_scope(request, sensorName):
    form = ScopeForm(request.POST or None)
    user = request.user
    #sensor = Sensor.objects.get(id=sensorName)
    #sensor = sensorName
    print "Sensor create: ",
    if form.is_valid():
        save_it = form.save(commit=False)
        save_it.idUser = user
        #save_it.sensor = sensor
        save_it.save()


def scope(request):
    measurement = {
            'tempMax': 0,
            'tempMin': 0,
            'humMax': 0,
            'humMin': 0,
    }
    state = False
    all_sensor = Sensor.objects.all()
    sensorName = None
    if request.POST:
        user = request.user
        sensor = request.POST.get('s', False)
        if sensor:
            sensorName= sensor
            sensorTmp = Sensor.objects.get(nameSensor=sensor)
            sensorSelected= Scope.objects.filter(sensor=sensorTmp.id, idUser=user).values()
            if sensorSelected:
                state=True
                measurement['tempMax'] = sensorSelected[0]['temp_max']
                measurement['tempMin'] = sensorSelected[0]['temp_min']
                measurement['humMax'] = sensorSelected[0]['hum_max']
                measurement['humMin'] = sensorSelected[0]['hum_min']

            else:
                return HttpResponseRedirect('/scope/form/'+str(sensorTmp.id))

    return render_to_response('scope.html', {'sensor':all_sensor, 'data': measurement,
                                             'state': state, 'sensorName': sensorName},
                              context_instance=RequestContext(request))


def formScope(request, pk):
    form = ScopeForm(request.POST or None)
    user = request.user
    sensorID = pk
    sensor = Sensor.objects.get(id=pk)
    userScope = Scope.objects.filter(idUser=user, sensor=sensor)

    if userScope:
        return HttpResponseRedirect('/scope')

    if form.is_valid():
        save_it = form.save(commit=False)
        save_it.idUser = user
        save_it.sensor=sensor
        save_it.save()
        return HttpResponseRedirect('/scope')
    return render_to_response('formScope.html',
                              {'idSensor': sensorID, 'form': form},
                              context_instance=RequestContext(request))

def deleteScope(request, nameSensor):
    user = request.user
    sensor = Sensor.objects.get(nameSensor=nameSensor)
    scope = Scope.objects.filter(idUser=user, sensor = sensor.id)
    scope.delete()
    return HttpResponseRedirect('/scope')
def contactHtml(request):
    return render(request, 'contact.html')