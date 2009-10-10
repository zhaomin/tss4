# Copyright (C) 2009 Software Institute, Nanjing University 

from tss4.core_app.models import Application

def app_list(request):
    """context processor that puts a list of available
       applications into the context"""
    from django.conf import settings
    return {'apps' : Application.objects.all(), 'MEDIA_URL': settings.MEDIA_URL}

