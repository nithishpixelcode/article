from django.conf.urls.defaults import patterns, include, url
from django.contrib import admin	
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns	

admin.autodiscover()

urlpatterns = patterns('',
    #reset password incase user forgets it ...
    url(r'^admin/password_reset/$', 'django.contrib.auth.views.password_reset', name='password_reset'),
    (r'^password_reset/done/$', 'django.contrib.auth.views.password_reset_done'),
    (r'^reset/(?P<uidb36>[0-9A-Za-z]+)-(?P<token>.+)/$', 'django.contrib.auth.views.password_reset_confirm'),
    (r'^reset/done/$', 'django.contrib.auth.views.password_reset_complete'),
    
    #registration and authentication
    url(r'^register/$', 'article.views.register', name='register'),
    url(r'^login/$', 'article.views.login', name='login'),
    url(r'^logout/$', 'article.views.logout', name='logout'),
    
    (r'^admin/', include(admin.site.urls)),
    url(r'^$', 'article.views.index', name='index'),
)

if settings.DEBUG:
    urlpatterns += patterns('',
        (r'^media/(?P<path>.*)$', 'django.views.static.serve',
         {'document_root': settings.MEDIA_ROOT}),
    )

