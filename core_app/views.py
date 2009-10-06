# Copyright (C) 2009 Software Institute, Nanjing University 

from django.shortcuts import render_to_response

from tss4.core_app.models import Application

def index(request):
    return render_to_response('index.html')
