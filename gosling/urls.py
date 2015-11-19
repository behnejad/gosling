from django.conf.urls import include, url
from django.contrib import admin
from dajaxice.core import dajaxice_autodiscover, dajaxice_config
from django.views.generic import TemplateView
from gosling import settings

dajaxice_autodiscover()
admin.autodiscover()

urlpatterns = (
    url(r'^', include('user.urls')),
    url(r'^policy/', TemplateView.as_view(template_name='policy.html'), name='policy'),
    url(r'^about/', TemplateView.as_view(template_name='about.html'), name='about'),
    url(r'^problem/', TemplateView.as_view(template_name='problem.html'), name='problem'),
    url(r'^addproblem/', TemplateView.as_view(template_name='addproblem.html'), name='addproblem'),
    url(r'^exam/', include('exam.urls')),
    url(dajaxice_config.dajaxice_url, include('dajaxice.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^doc/', include('django.contrib.admindocs.urls')),
    url(r'^statics/(?P<path>.*)$', 'django.views.static.serve',
        {'document_root': settings.STATICFILES_DIRS[0], 'show_indexes': False}),
)
