from django.conf.urls import patterns, url

from testapp import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^json/towns$', views.json_towns)
)