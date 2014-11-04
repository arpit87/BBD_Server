from django.conf.urls import patterns,url

from User import views

urlpatterns = patterns('',
                       url(r'^createUser/',views.createUser,name='createUser'),
                       url(r'^addFriend/',views.addFriend,name='addFriend'),
                    )