from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.views.generic import TemplateView

from dajaxice.core import dajaxice_autodiscover, dajaxice_config

dajaxice_autodiscover()
admin.autodiscover()

<<<<<<< HEAD
urlpatterns = patterns('',
	(r'^', include('user.urls')),
	(dajaxice_config.dajaxice_url, include('dajaxice.urls')),
    (r'^admin/', include(admin.site.urls)),
    (r'^doc/', include('django.contrib.admindocs.urls')),
=======
urlpatterns = (
	url(r'^$', include('user.urls')),
    url(r'^exam/', include('exam.urls')),
	url(dajaxice_config.dajaxice_url, include('dajaxice.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^doc/', include('django.contrib.admindocs.urls')),
>>>>>>> cd0f8ab826dcb62e2400a74accdb9dde9a501757
)
