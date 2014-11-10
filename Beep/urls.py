from django.conf.urls import patterns,url
from Beep import views

urlpatterns = patterns('',
                       url(r'^getBeep/',views.getBeep,name='getbeep'),
                       url(r'^createBeep/',views.createBeep,name='createBeep'),
                       url(r'^getBeepList/',views.getBeepList,name='getBeepList'),
                       url(r'^getMyBeepList/',views.getMyBeepList,name='getMyBeepList'),
                       url(r'^sendBeep/',views.sendBeep,name='sendBeep'),
                        )