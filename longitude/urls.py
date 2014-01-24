from django.conf.urls import patterns, url
from longitude import views

urlpatterns = patterns(' ',
                       url(r'^$',views.index, name='longitude.index'),
                       url(r'^(?P<brand_pk>\d+)/$', views.detail, name='longitude.detail'),
                       #url(r'^search/$', views.search, name='longitude.search_form'),


)