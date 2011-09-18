
from django.conf.urls.defaults import patterns, include, url
from django.contrib import admin	
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns	

# Uncomment the next two lines to enable the admin:

admin.autodiscover()

urlpatterns = patterns('',
    # Example:
    # (r'^{{ project_name }}/', include('{{ project_name }}.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    (r'^admin/', include(admin.site.urls)),
    url(r'^$', 'article.views.index', name='index'),
)

if settings.DEBUG:
    urlpatterns += patterns('',
        (r'^media/(?P<path>.*)$', 'django.views.static.serve',
         {'document_root': settings.MEDIA_ROOT}),
    )

