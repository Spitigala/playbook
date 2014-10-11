from django.conf.urls import url
from players import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^players/$', views.players, name='players'),
    url(r'^players/create/$', views.create, name='create'),
    url(r'^players/edit/(?P<player_id>\d+)/$', views.edit, name='edit'),
    url(r'^players/delete/(?P<player_id>\d+)/$', views.delete, name='delete'),
]