from django.test import TestCase
from django.test.client import RequestFactory

from measurement.views import measurement
from measurement.models import  Sensor, Rooms, MeasurementData

import json
import mock


# Create your tests here.
class MeasurementsTests(TestCase):

    def setUp(self):
        Rooms.objects.create(nameRoom='pokoj1')
        r1 = Rooms.objects.get(id=1)
        Sensor.objects.create(nameSensor='Sensor1', idRoom=r1)

    @mock.patch('measurement.views.MeasurementData')
    def test_add_mesurment_fail_not_json(self, mock_measdata):
        m1_str = 'ala_ma_kota=1'

        rf = RequestFactory()
        req1 = rf.post('/measurement/', data=m1_str, content_type="application/json")

        measurement(req1)

    def test_add_mesurment_fail_invalid_sensor(self):
        m1 = {
            'timestamp': '2015-02-22',
            'temperature': '21.2',
            'humidity': '60.2',
            'idSensor': 2
        }
        m1_str = json.dumps(m1)

        rf = RequestFactory()
        req1 = rf.post('/measurement/', data=m1_str, content_type="application/json")

        res = measurement(req1)
        d = json.loads(res.content)

        self.assertEqual(d['status'], 'fail')


    def test_add_mesurment_ok_add_new(self):
        m2 = {
            'timestamp': '2015-03-29 18:23:50.965672',
            'temperature': '22.2',
            'humidity': '60.2',
            'idSensor': '1'
        }
        m2_str = json.dumps(m2)

        rf = RequestFactory()
        req2 = rf.post('/measurement/', data=m2_str, content_type="application/json")

        res = measurement(req2)
        d = json.loads(res.content)

        self.assertEqual(d['status'], 'ok')
        print MeasurementData.objects.all()
