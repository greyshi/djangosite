from django.conf.urls import patterns, url, include

from polls import views

urlpatterns = patterns('',
                       url(r'^$', views.index, name='index'),
                       url(r'(?P<poll_id>\d+)/$', views.detail, name='detail'),
                       url(r'(?P<poll_id>\d+)/vote/$', views.vote, name='vote'),
                       url(r'create/$', views.create, name='create'),
                       url(r'(?P<poll_id>\d+)/results/$', views.results, name='results'),
                       )
