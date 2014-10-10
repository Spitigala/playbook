from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'playbook.views.home', name='home'),

    # url(r'^$', include('players.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^players/', include('players.urls')),
    # url(r'^players/', 'players.views.players'),
)

# for root url, you can't handle it through player.