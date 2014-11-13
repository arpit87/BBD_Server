from django.conf.urls import patterns,url
from Trends import views

urlpatterns = patterns('',
                       url(r'^getTimeTrends/',views.getTimeTrends,name='getTimeTrends'),
                       url(r'^updateTimeTrends/',views.updateTimeTrends,name='updateTimeTrends')
                        )