from django.contrib import admin

from measurement.models import MeasurementData, Rooms, Sensor

class MeasurementAdmin(admin.ModelAdmin):
    list_display = ('idSensor','timestamp', 'temperature', 'humidity')

admin.site.register(MeasurementData, MeasurementAdmin)

admin.site.register(Rooms)

admin.site.register(Sensor)