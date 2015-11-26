from django.conf.urls import url
from exam import views


urlpatterns = (
    url(r'^$', views.index, name='examIndex'),
    url(r'^exam/(?P<eID>\d{1,4})$', views.exam, name='exam'),
    url(r'^examList/$', views.exam_list, name='examList'),
    url(r'^group/(?P<eID>\d{1,4})$', views.group, name='group'),
    url(r'^groupList/$', views.group_list, name='groupList'),
    url(r'^problemList/$', views.problem_list, name='problemList'),
    url(r'^problem/$', views.problem, name='Problem'),
    url(r'^addproblem/$', views.add_problem, name='addProblem'),
    url(r'^loginGroup/$', views.loginGroup, name='loginGroup'),
    url(r'^createGroup/$', views.createGroup, name='createGroup'),
    url(r'^group/$', views.group, name='group'),
)
