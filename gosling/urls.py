from django.conf.urls import include, url
from django.contrib import admin
from dajaxice.core import dajaxice_autodiscover, dajaxice_config
from django.views.generic import TemplateView
from views import policy, about

dajaxice_autodiscover()
admin.autodiscover()

urlpatterns = (
    url(r'^$', TemplateView.as_view(template_name='index.html'), name='home'),
    url(r'^policy/', policy, name='policy'),
    url(r'^about/', about, name='about'),
    url(r'^user/', include('user.urls')),
    url(r'^exam/', include('exam.urls')),
    url(dajaxice_config.dajaxice_url, include('dajaxice.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^doc/', include('django.contrib.admindocs.urls')),
)
