from django.conf.urls import url
from exam import views


urlpatterns = (
    url(r'^$', views.index, name='index'),
    url(r'^List/$', views.list, name='exam list'),
    url(r'^Groups/$', views.group, name='exam group'),
    url(r'^Problems/$', views.problems, name='exam problem'),
)
