# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('measurement', '0002_rooms_sensor'),
    ]

    operations = [
        migrations.AddField(
            model_name='measurementdata',
            name='idSensor',
            field=models.ForeignKey(default=1, to='measurement.Sensor'),
            preserve_default=False,
        ),
    ]
