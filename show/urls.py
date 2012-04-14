from django.conf.urls import *

urlpatterns = patterns('show.views',
    url(r'^add/', 'add'),
    url(r'^auto/', 'auto'),
)
