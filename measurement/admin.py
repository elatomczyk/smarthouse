from django.contrib import admin

from measurement.models import MeasurementData

class MeasurementAdmin(admin.ModelAdmin):
    list_display = ('timestamp', 'temperature', 'humidity')

admin.site.register(MeasurementData, MeasurementAdmin)

