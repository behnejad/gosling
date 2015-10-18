from django.conf.urls import patterns, include, url
from exam import views

urlpatterns = (
    url(r'^$', views.index, name='home'),
    url(r'^List/$', views.list, name='exam list'),
    url(r'^Groups/$', views.group, name='exam group'),
    url(r'^Problems/$', views.problems, name='exam problem'),
)



