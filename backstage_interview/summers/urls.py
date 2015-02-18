from django.conf.urls import patterns, url

from summers import views

urlpatterns = patterns('',
    url(r'^difference$', views.difference, name='difference')
)
