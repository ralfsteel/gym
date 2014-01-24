from django.conf.urls import patterns, include, url
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
     url(r'^longitude/', include('longitude.urls')),
     url(r'^mygym/', include('mygym.urls')),


    url(r'^admin/', include(admin.site.urls)),
)

