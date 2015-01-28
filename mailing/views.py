from threading import Thread
from django.contrib.auth.models import User
from django.template import Context
from django.template.loader import get_template
from django.core.mail import EmailMessage
from measurement.models import MeasurementData, Sensor, Scope
from django.http import HttpResponseRedirect
import time


def email(user):
    user_name = User.objects.filter(username=user)[0]
    mail = user_name.email
    measurement = MeasurementData.objects.order_by('timestamp').values().last()
    temperature=measurement['temperature']
    humidity=measurement['humidity']
    timestamp=measurement['timestamp']
    id_m=measurement['idSensor_id']
    #print measurement
    id_s=Sensor.objects.get(id=id_m)
    name_sensor = id_s.nameSensor
    room_name = id_s.idRoom        
    subject = "Informacje ze strony Smarthouse"
    to = [mail]
    from_email = 'smarthousekrakow@gmail.com'   
    ctx = {
           'user': user_name,
           'temperature': temperature,
           'humidity': humidity,
           'timestamp': timestamp,
           'room_name': room_name,
           'name_sensor': name_sensor
    }
    message = get_template('email.html').render(Context(ctx))
    msg = EmailMessage(subject, message, to=to, from_email=from_email)
    msg.content_subtype = 'html'
    print user_name.id
    scope = Scope.objects.get(idUser=user_name.id)

    t_max = scope.temp_max 
    t_min = scope.temp_min
    h_max = scope.hum_max
    h_min = scope.hum_min
    if(temperature>t_max or temperature<t_min) or (humidity>h_max or humidity<h_min):
        print"Send Mail to ", user_name
        msg.send()
    else:
        print"No Send Mail"
    return HttpResponseRedirect('/')


def usermethod():
    for s in Scope.objects.all():
        #print "def usermethod(): ", s.idUser

        userid = s.idUser
        email(userid)


class MyThread(Thread):
    def __init__(self):
        Thread.__init__(self)
        self.daemon = True

    def run(self, stop=False):

        while True:
            usermethod()
            time.sleep(43200)


def threadmethod():
    try:
        thread1 = MyThread()
        thread1.start()
    except StandardError:
        print "Ctrl-c pressed ..."
        thread1.stop()



