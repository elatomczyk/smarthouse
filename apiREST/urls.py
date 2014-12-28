from django.conf.urls import patterns, include, url

from apiREST import views

urlpatterns = patterns('',

    url(r'^$', views.MeasurementDataREST.as_view(), name='RestNumber'),
    url(r'^login/$', views.login),


)