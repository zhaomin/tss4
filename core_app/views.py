# Copyright (C) 2009 Software Institute, Nanjing University 

from django.shortcuts import render_to_response

def index(request):
    return render_to_response('index.html')
