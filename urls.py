# Copyright (C) 2009 Software Institute, Nanjing University 

from django.conf.urls.defaults import *
from django.conf import settings

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = []
if settings.DEBUG:
    urlpatterns = patterns('',
        (r'^%s(?P<path>.*)$' % settings.MEDIA_URL[1:], 'django.views.static.serve',
                {'document_root' : settings.MEDIA_ROOT}),
    )

urlpatterns += patterns('',
    # Example:
    (r'^service/', include('tss4.service_app.urls')),
    (r'^', include('tss4.core_app.urls')),

    # Uncomment the admin/doc line below and add 'django.contrib.admindocs' 
    # to INSTALLED_APPS to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # (r'^admin/(.*)', admin.site.root),
)


