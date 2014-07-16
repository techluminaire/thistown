from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'Core.views.index_views.index', name='index'),
    #url(r'^music/', 'Core.views.index_views.music', name='music'),
    #url(r'^film/', 'Core.views.index_views.film', name='film'),
    #url(r'^eat/', 'Core.views.index_views.eat', name='eat'),
    #url(r'^people/', 'Core.views.index_views.people', name='people'),

    url(r'^admin/', include(admin.site.urls)),
)
