from django.conf.urls import url

from players import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^$', views.players, name='players'),
]