# Copyright (C) 2009 Software Institute, Nanjing University 

from django.views.generic.simple import direct_to_template

def index(request):
    return direct_to_template(request, 'index.html')

def load_app(request, app):
    return direct_to_template(request, 'app_index.html', {'app_name' : app})
