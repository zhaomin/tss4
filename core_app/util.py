# Copyright (C) 2009 Software Institute, Nanjing University 

from tss4.core_app.models import Application

def media(request):
    """the default media context processor seems not working. this is
       a hack"""
    from django.conf import settings
    return {'MEDIA_URL' : settings.MEDIA_URL}

def app_list(request):
    """context processor that puts a list of available
       applications into the context"""
    return {'apps' : Application.objects.all()}

