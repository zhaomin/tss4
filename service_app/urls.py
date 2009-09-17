# Copyright (C) 2009 Software Institute, Nanjing University 

from django.conf.urls.defaults import *

urlpatterns = patterns('tss4.service_app.views',
    (r'^(.+?)/$', 'service'),
)
