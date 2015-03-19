from threading import Thread
from django.contrib.auth.models import User
from django.template import Context
from django.template.loader import get_template
from django.core.mail import EmailMessage
from measurement.models import MeasurementData, Sensor, Scope
from django.http import HttpResponseRedirect
import time


def email():
    for s in Scope.objects.all():
        user_name = User.objects.filter(username=s.idUser)[0]
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
        # print user_name.id
        t_max = s.temp_max
        t_min = s.temp_min
        h_max = s.hum_max
        h_min = s.hum_min
        if(temperature>t_max or temperature<t_min) or (humidity>h_max or humidity<h_min):
            d = dict()
            if(temperature>t_max):
                difference1=temperature-t_max
                d = {'Temperatura makasymalna':difference1}
            elif(temperature<t_min):
                difference1=temperature-t_min
                d = {'Temperatura minimalna':difference1}
            if(humidity>h_max):
                difference2=humidity-h_max
                d.update({'Wilgotnosc maksymalna':difference2})
            elif(humidity<h_min):
                difference2=humidity-h_min
                d.update({'Wilgotnosc minimalna':difference2})
            print"Send Mail to ", user_name
            ctx = {
                   'user': user_name,
                   'difference': d.values(),
                   'what': d.keys(),
                   'temperature': temperature,
                   'humidity': humidity,
                   'timestamp': timestamp,
                   'room_name': room_name,
                   'name_sensor': name_sensor
            }
            message = get_template('email.html').render(Context(ctx))
            msg = EmailMessage(subject, message, to=to, from_email=from_email)
            msg.content_subtype = 'html'
            msg.send()
        else:
            print"No Send Mail"
    return HttpResponseRedirect('/')


class MyThread(Thread):
    def __init__(self):
        Thread.__init__(self)
        self.daemon = True

    def run(self, stop=False):

        while True:
            email()
            time.sleep(600)


def threadmethod():
    try:
        thread1 = MyThread()
        thread1.start()
    except StandardError:
        print "Ctrl-c pressed ..."
        thread1.stop()



