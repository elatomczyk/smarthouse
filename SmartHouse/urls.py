from django.conf.urls import patterns, include, url
from django.contrib import admin
from measurement import views
from django.conf import settings
from django.conf.urls.static import static

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', views.index, name='home'),
    url(r'^admin/', include(admin.site.urls)),
    #DjangoREST
    url(r'^rest/', include('apiREST.urls')),
    #czujnik przesyla dane pod adres ponizej
    url(r'^measurement/', views.measurement),
    url(r'^diagram/$', views.diagram, name="diagram"),
    #login and logout
    url(r'^login/$','django.contrib.auth.views.login',{'template_name': 'login.html'}, name='login'),
    url(r'^logout/$', 'account.views.logout_page', name='logout'),
    #register
    url(r'^register/$', 'account.views.register_user', name='register'),
    url(r'^register/register_success/$', 'account.views.register_success'),
    #temperature and humidity scope
    url(r'^scope/$',views.scope, name="scope"),
    url(r'^scope/form/(?P<pk>\d+)/$', views.formScope, name='formScope'),
    url(r'^scope/form/(?P<nameSensor>[0-9a-zA-Z  _-]+)/$', views.deleteScope, name='deleteScope'),
)

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
