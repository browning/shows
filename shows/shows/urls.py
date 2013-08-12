from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView
from showlist import views

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'showlist.views.index'),

    # Examples:
    # url(r'^$', 'shows.views.home', name='home'),
    # url(r'^shows/', include('shows.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
