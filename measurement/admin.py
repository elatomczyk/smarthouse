from django.contrib import admin

from measurement.models import MeasurementData, Rooms, Sensor, Scope

class MeasurementAdmin(admin.ModelAdmin):
    list_display = ('idSensor', 'timestamp', 'temperature', 'humidity')

admin.site.register(MeasurementData, MeasurementAdmin)

admin.site.register(Rooms)

admin.site.register(Sensor)

class ScopeAdmin(admin.ModelAdmin):
    list_display = ('hum_min', 'hum_max', 'temp_min', 'temp_max', 'idUser')

admin.site.register(Scope,ScopeAdmin)