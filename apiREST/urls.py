from django.conf.urls import patterns, include, url

from apiREST import views

urlpatterns = patterns('',

    url(r'^$', views.MeasurementDataREST.as_view(), name='RestNumber'),
    url(r'^graph/(?P<limit>\d+)', views.MeasurementGraphREST.as_view(), name='RestGraph'),
    url(r'^sensor/$', views.SensorREST.as_view(), name='RestSensor'),
    url(r'^login/$', views.login),


)