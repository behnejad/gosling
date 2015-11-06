from django.conf.urls import url
from exam import views


urlpatterns = (
    url(r'^$', views.index, name='index'),
    url(r'^exam/$', views.exam, name='exam'),
    url(r'^examList/$', views.exam_list, name='exam list'),
    url(r'^group/$', views.group, name='group'),
    url(r'^groupList/$', views.group_list, name='group list'),
    url(r'^problem/$', views.problem, name='exam problem'),
)
