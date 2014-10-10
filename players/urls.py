from django.conf.urls import url
from players import views

urlpatterns = [
    url(r'^$', views.players, name='players'),
    url(r'^create/$', views.create, name='create'),
    url(r'^edit/(?P<player_id>\d+)/$', views.edit, name='edit'),
    url(r'^delete/(?P<player_id>\d+)/$', views.delete, name='delete'),
]