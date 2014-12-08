# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MeasurementData',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('timestamp', models.DateTimeField()),
                ('temperature', models.FloatField(default=-100.0)),
                ('humidity', models.FloatField(default=-100.0)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
