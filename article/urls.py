
from django.conf.urls.defaults import patterns, include, url
from django.contrib import admin	
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns	

admin.autodiscover()

urlpatterns = patterns('',
    #authentication
    url(r'^login/$', 'article.views.login', name='login'),
    
    (r'^admin/', include(admin.site.urls)),
    url(r'^$', 'article.views.index', name='index'),
)

if settings.DEBUG:
    urlpatterns += patterns('',
        (r'^media/(?P<path>.*)$', 'django.views.static.serve',
         {'document_root': settings.MEDIA_ROOT}),
    )

