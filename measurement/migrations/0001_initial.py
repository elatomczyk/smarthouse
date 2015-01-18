# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
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
        migrations.CreateModel(
            name='Rooms',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nameRoom', models.CharField(max_length=100)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Scope',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('hum_min', models.FloatField(default=15)),
                ('hum_max', models.FloatField(default=100, max_length=100)),
                ('temp_min', models.FloatField(default=5)),
                ('temp_max', models.FloatField(default=60, max_length=100)),
                ('idUser', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Sensor',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nameSensor', models.CharField(max_length=100)),
                ('idRoom', models.ForeignKey(to='measurement.Rooms')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='scope',
            name='sensor',
            field=models.ForeignKey(to='measurement.Sensor'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='measurementdata',
            name='idSensor',
            field=models.ForeignKey(to='measurement.Sensor'),
            preserve_default=True,
        ),
    ]
