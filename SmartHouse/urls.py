from django.conf.urls import patterns, include, url
from django.contrib import admin
from measurement import views
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
    #wskaznik temperatury
    url(r'^scope/$',views.create_scope, name="scope")
)
