from django.conf.urls import patterns, include, url
import django.contrib.auth
import django.contrib.auth.views

#from django.contrib import admin
#admin.autodiscover()

urlpatterns = patterns('',
    #url(r'^admin/', include(admin.site.urls)),
	url(r'^',include('flights.urls')),
    (r'^selectable/', include('selectable.urls')),
)
