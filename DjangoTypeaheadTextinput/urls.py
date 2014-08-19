from django.conf.urls import patterns, include, url
from django.views.generic.base import RedirectView

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'CustomTags.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^typeahead/', include('testapp.urls', namespace="Typeahead")),
    url(r'^$', RedirectView.as_view(url='/typeahead/')),
)