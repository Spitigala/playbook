from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^players/', include('players.urls')),
)

# for root url, you can't handle it through player.