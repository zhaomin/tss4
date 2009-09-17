# Copyright (C) 2009 Software Institute, Nanjing University 

from django.http import HttpResponse

from tss4 import ws

def service(request, cmd):
    handler = ws.find_handler(cmd)
    if handler:
        return handler.handle(request)
    else:
        return HttpResponse('cmd %s not found' % cmd)


