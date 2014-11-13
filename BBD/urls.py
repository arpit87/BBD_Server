from django.conf.urls import patterns, include, url

from django.contrib import admin


admin.autodiscover()

urlpatterns = patterns('',

                       url(r'^admin/', include(admin.site.urls)),
                       url(r'^Beep/',include('Beep.urls')),
                       url(r'^User/',include('User.urls')),
                       url(r'^Chat/',include('Chat.urls')),
                       url(r'^Trends/',include('Trends.urls')),
                       url(r'',include('Platform.urls')),
                      )







