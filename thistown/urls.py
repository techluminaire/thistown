from django.conf.urls import patterns, include, url
from django.conf import settings
from django.contrib import admin
from articles.admin.admin_site import admin_site

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'articles.views.index_views.index', name='index'),
    url(r'^admin/', include(admin_site.urls)),
    url(r'^search','articles.views.search_results', name='search'),
    url(r'^articles/(?P<article_name>\w+)/$','articles.views.article_view', name='article'),
    #url(r'^whatson/', 'calendar.views.index_views.calendar_index', name='calendar_index'),
    url(r'^(?P<category_name>\w+)/$', 'articles.views.index_views.category_index', name='category_index'),
    url(r'^(?P<category_name>\w+)/(?P<sub_category_name>\w+)/$', 'articles.views.index_views.sub_category_index', name='sub_category_index'),
)


#Allow media to be served in debug mode
if settings.DEBUG:
    urlpatterns += patterns('',
        (r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
    )