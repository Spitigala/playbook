from django.conf.urls import url
from players import views

urlpatterns = [
    url(r'^$', views.players, name='players'),
    url(r'^create/$', views.create, name='create'),
    # url(r'^create/$', views.create, name='create'),
    # url(r'^$', views.index, name='index'),
]