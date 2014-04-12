from django.conf.urls import patterns, url, include
from flights import views
#import django.contrib.auth.views


urlpatterns = patterns('flights.views',
    url(r'^$', 'home'),
    url(r'^register/$', 'register',name='signup'),
    url(r'^login/$', 'login', name='login'),
    url(r'^about/$', 'about'),
    url(r'^savesearch/$', 'saveSearch'),
    url(r'^searches/$', 'searches'),
)

urlpatterns += patterns('',
  url(r'^logout/$', 'django.contrib.auth.views.logout', {'next_page': '/'},name='logout'),
  #url(r'^api/get_airports/$','flights.views.get_airports', name='get_airports'),
  #(r'^selectable/', include('selectable.urls')),
)