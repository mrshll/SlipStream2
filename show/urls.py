from django.conf.urls import *

urlpatterns = patterns('show.views',
    url(r'^add_show/', 'add_show'),
    url(r'^add_provider/', 'add_provider'),
    url(r'^auto/', 'auto'),
)
