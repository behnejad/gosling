from django.conf.urls import url
from exam import views


urlpatterns = (
    url(r'^$', views.index, name='examIndex'),
    url(r'^exam/(?P<eID>\d{1,4})$', views.exam, name='exam'),
    url(r'^examMake/(?P<eID>\d{1,4})$', views.selectQuestions, name='selectQuestion'),
    url(r'^makeExam$', views.makeExam, name='makeExam'),
    url(r'^examList/$', views.exam_list, name='examList'),
    url(r'^group/(?P<eID>\d{1,4})$', views.group, name='group'),
    url(r'^groupAdd$', views.addToGroup, name='addToGroup'),
    url(r'^groupList/$', views.group_list, name='groupList'),
    url(r'^problemList/$', views.problem_list, name='problemList'),
    url(r'^problem/$', views.problem, name='Problem'),
    url(r'^addproblem/$', views.add_problem, name='addProblem'),
    url(r'^loginGroup/(?P<gId>\d{1,4})$', views.loginGroup, name='loginGroup'),
    url(r'^createGroup/$', views.createGroup, name='createGroup'),
    url(r'^admin/(?P<gId>\d{1,4})$', views.admin, name='groupAdmin'),
    url(r'^answer/set$', views.answerProblem, kwargs={'mode': 'set'}, name='answerProblem'),
    url(r'^answer/del$', views.answerProblem, kwargs={'mode': 'del'}, name='answerProblemDelete'),
)
