from django.conf.urls import patterns,url
from Platform import views

urlpatterns = patterns('',
                      url(r'',views.index,name='index'),
                      )
