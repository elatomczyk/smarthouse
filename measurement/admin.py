from django.contrib import admin

from measurement.models import MeasurementData, Rooms, Sensor, Scope

class MeasurementAdmin(admin.ModelAdmin):
    list_display = ('timestamp', 'temperature', 'humidity')

admin.site.register(MeasurementData, MeasurementAdmin)

admin.site.register(Rooms)

admin.site.register(Sensor)

admin.site.register(Scope)