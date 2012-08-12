from django.conf.urls.defaults import patterns, include, url

from main_site import views

import dselector
parser = dselector.Parser()
url = parser.url

urlpatterns = patterns('',
    url(r'^$', views.home, name='home'),
    url(r'^daily', views.daily, name='daily'),
    url(r'^monthly', views.monthly, name='monthly'),
    url(r'^update_bumpers/{bumper_pk:digits}/', views.update_bumpers, name='update_bumpers'),
)
