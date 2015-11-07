from django.conf.urls import url
import views

urlpatterns = (
    url(r'^$', views.index, name='index'),
    url(r'^profile/$', views.profile, name='profile'),
    url(r'^login/$', views.login, name='login'),
    url(r'^logout/$', views.logout, name='logout'),
    url(r'^register/$', views.register, name='register'),
    url(r'^forgot/$', views.forgot, name='forgot'),
    url(r'^doreg/$', views.do_reg, name='doReg'),
    url(r'^password_change/$', views.password_change, name='passwordChange'),
    url(r'^password_change/done/$', views.password_change_done, name='passwordChangeDone'),
    url(r'^password_reset/$', views.password_reset, name='passwordReset'),
    url(r'^password_reset/done/$', views.password_reset_done, name='passwordResetDone'),
    url(r'^reset/done/$', views.password_reset_complete, name='passwordResetComplete'),
    url(r'^close/$', views.close, name='close'),
)
