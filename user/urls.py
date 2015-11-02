from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView
import views

urlpatterns = (
    url(r'^$', TemplateView.as_view(template_name='index.html'), name='index'),
    url(r'^home/$', views.home, name='home'),
    url(r'^profile/$', views.profile, name='profile'),
    url(r'^login/$', views.login, name='login'),
    url(r'^logout/$', views.logout, name='logout'),
    url(r'^register/$', views.register, name='signup'),
    url(r'^forgot/$', views.forgot, name='forgot'),
    url(r'^doreg/$', views.doreg, name='forgot'),
    url(r'^password_change/$', views.password_change, name='password_change'),
    url(r'^password_change/done/$', views.password_change_done, name='password_change_done'),
    url(r'^password_reset/$', views.password_reset, name='password_reset'),
    url(r'^password_reset/done/$', views.password_reset_done, name='password_reset_done'),
    url(r'^reset/done/$', views.password_reset_complete, name='password_reset_complete'),
)
