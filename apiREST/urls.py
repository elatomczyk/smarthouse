from django.conf.urls import patterns, include, url
from django.contrib import admin
from apiREST import views

urlpatterns = patterns('',

    url(r'^$', views.MeasurementDataREST.as_view(), name='RestNumber'),

)