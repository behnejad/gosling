from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.views.generic import TemplateView

from dajaxice.core import dajaxice_autodiscover, dajaxice_config

dajaxice_autodiscover()
admin.autodiscover()

urlpatterns = patterns('',
	(r'^$', include('user.urls')),


	(dajaxice_config.dajaxice_url, include('dajaxice.urls')),
    (r'^admin/', include(admin.site.urls)),
    (r'^doc/', include('django.contrib.admindocs.urls')),
)
