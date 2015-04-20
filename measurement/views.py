import json
from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist, ValidationError
from django.shortcuts import render_to_response, render
from django.template import RequestContext
from django.utils.dateformat import DateFormat
from measurement.models import MeasurementData, Sensor, Scope, Rooms
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from measurement.forms import ScopeForm
from mailing.views import threadmethod
from django.http import HttpResponseRedirect

#metoda do wysywania maili
# threadmethod()


def index(request):
    sensor = Sensor.objects.all()
    data = []
    for s in sensor:
        m = MeasurementData.objects.filter(idSensor=s).order_by('timestamp').last()
        if m:
            data.append(MeasurementClass(m.timestamp, m.temperature, m.humidity, m.idSensor, s.idRoom))
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
    try:

        if request.method == 'POST':
            d = json.loads(request.body)
            print json.loads(request.body)
            sensor = Sensor.objects.get(id=int(d['idSensor']))
            m = MeasurementData(
                            timestamp=d['timestamp'],
                            temperature=d['temperature'],
                            humidity=d['humidity'],
                            idSensor=sensor)

            m.save()
            print 'dasas'
            return JsonResponse({'status': 'ok'})

    except ValueError, e:
        print 'dasas2'
        return JsonResponse({'status': 'fail'})
    except ObjectDoesNotExist:
        print 'dasas'
        return JsonResponse({'status': 'fail'})
    finally:
        print 'koniec'


def diagram(request):
    data = []
    rooms = Rooms.objects.all()

    try:
        if request.POST:
            roomsPOSTGraph = request.POST.get('r', False)
            roomsName = Rooms.objects.get(nameRoom=roomsPOSTGraph)
            date_start = request.POST.get('dateStart', False)
            date_end = request.POST.get('dateEnd', False)

            for s in Sensor.objects.all():
                if roomsName == s.idRoom:
                    measurement_graph = MeasurementData.objects.filter(idSensor=s.id, timestamp__gte=date_start,
                                                                       timestamp__lte=date_end)
                    for m in measurement_graph:

                        data.append(MeasurementClass(m.timestamp, m.temperature, m.humidity, m.idSensor, roomsName))
            text = "----"
            first_data = date_start
            last_data = date_end
        else:
            text = "Wszystkie Pomiary"
            sensor = Sensor.objects.get(id=1)
            roomsName = sensor.idRoom
            data = MeasurementData.objects.filter(idSensor=1)

            df = DateFormat(data[0].timestamp)
            first_data = df.format('Y-m-d')
            df2 = DateFormat(data[len(data)-1].timestamp)
            last_data = df2.format('Y-m-d')

    except ObjectDoesNotExist:
        textproblem = "Prosze o wybranie czujnika."
        return render(request, 'diagram.html', {'problem': textproblem, 'rooms': rooms})
    except ValidationError as e:
        textproblem = "Prosze o wybranie daty."
        return render(request, 'diagram.html', {'problem': textproblem, 'rooms': rooms})

    return render_to_response('diagram.html', {'data': data, 'rooms': rooms, 'text': text, 'roomName': roomsName,
                                               'firstData': first_data, 'lastData': last_data}, context_instance=RequestContext(request))


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


class MeasurementClass():
    timestamp = ""
    temperature = ""
    humidity = ""
    idSensor = ""
    room = ""

    def __init__(self, time, temp, hum, senor, room):
        self.timestamp = time
        self.temperature = temp
        self.humidity = hum
        self.idSensor = senor
        self.room = room
