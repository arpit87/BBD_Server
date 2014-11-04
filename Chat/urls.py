from django.conf.urls import patterns,url
from Chat import views

urlpatterns = patterns('',
                      url(r'^createChatUser/',views.createChatUser,name='createChatUser'),
                      )