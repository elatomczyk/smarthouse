# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('measurement', '0004_scope'),
    ]

    operations = [
        migrations.AlterField(
            model_name='scope',
            name='hum_max',
            field=models.FloatField(default=100, max_length=100),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='scope',
            name='hum_min',
            field=models.FloatField(default=15),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='scope',
            name='temp_max',
            field=models.FloatField(default=60, max_length=100),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='scope',
            name='temp_min',
            field=models.FloatField(default=5),
            preserve_default=True,
        ),
    ]
