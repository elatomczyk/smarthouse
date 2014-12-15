from django.conf.urls import patterns, include, url
from django.contrib import admin
from measurement import views

urlpatterns = patterns('',
    # Examples:
    url(r'^$', views.index, name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^rest/', include('apiREST.urls')),
    #czujnik przesyla dane pod adres ponizej
    url(r'^measurement/', views.measurement),

    url(r'^diagram/$', views.diagram, name="diagram"),

)
