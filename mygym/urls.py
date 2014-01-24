from django.conf.urls import patterns, include, url

from mygym import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='gym.index'),

    url(r'^(?P<_id>\d+)/$', views.detail, name='gym.detail'),

    #url(r'^(?P<training_routine>\d+)/results/$', views.results, name='results'),

)
