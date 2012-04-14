from django.conf.urls import patterns, include, url
from SlipStream import settings

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
        # show
        url(r'^$', 'show.views.home', name='home'),

        # static/media routes
        url(r'^static/(?P<path>.*)$', 'django.views.static.serve',
            {'document_root':settings.STATIC_ROOT}),
        url(r'^media/(?P<path>.*)$', 'django.views.static.serve',
            {'document_root':settings.MEDIA_ROOT}),

        # admin
        url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
        url(r'^admin/', include(admin.site.urls)),
)
