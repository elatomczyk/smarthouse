from django.conf.urls import patterns, include, url

from apiREST import views

urlpatterns = patterns('',

    url(r'^$', views.MeasurementDataREST.as_view(), name='RestNumber'),
    #TODO problem z polskimi znakami i jesli wystapi spacja
    url(r'^graph/(?P<nameSensor>[0-9a-zA-Z  _-]+)/(?P<limit>\d+)', views.MeasurementGraphREST.as_view(), name='RestGraph'),
    url(r'^sensor/$', views.SensorREST.as_view(), name='RestSensor'),
    url(r'^login/$', views.login),
    url(r'^scope/(?P<username>[0-9a-zA-Z  _-]+)/$', views.CheckScope.as_view(), name='RestScope'),

)