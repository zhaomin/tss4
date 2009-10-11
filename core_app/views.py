# Copyright (C) 2009 Software Institute, Nanjing University 

from django.shortcuts import get_object_or_404
from django.views.generic.simple import direct_to_template

import urllib

from tss4.core_app.models import Application

def index(request):
    return direct_to_template(request, 'index.html')

def service_app(request, app, path):
    app_obj = get_object_or_404(Application, unix_name=app)
    # TODO: check permission

    # make a remote request to the app site
    f = urllib.urlopen(app_obj.link)
    data = f.read()
    return direct_to_template(request, 'app_index.html',
            {'app' : app_obj,
             'content' : data,
            })
