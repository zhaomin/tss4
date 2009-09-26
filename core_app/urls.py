# Copyright (C) 2009 Software Institute, Nanjing University 

from django.conf.urls.defaults import *

urlpatterns = patterns('tss4.core_app.views',
    (r'^$', 'index'),
    (r'^index.html$', 'index'),
)

