from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'articles.views.index_views.index', name='index'),
    url(r'^admin/', include(admin.site.urls)),
    #url(r'^whatson/', 'calendar.views.index_views.calendar_index', name='calendar_index'),
    url(r'^(?P<category_name>\w+)/$', 'articles.views.index_views.category_index', name='category_index'),
    url(r'^(?P<category_name>\w+)/(?P<sub_category_name>\w+)/$', 'articles.views.index_views.sub_category_index', name='sub_category_index'),
)
