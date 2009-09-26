# Copyright (C) 2009 Software Institute, Nanjing University 

from django.http import HttpResponse

from tss4 import ws

def service(request, cmd):
    handler = ws.find_handler(cmd)
    if handler:
        entities = [x for x in request.path.split('/') if x <> '']
        entities = entities[2:]
        params = {}
        # XXX only convert unicode within ASCII range to str
        if request.method == "GET":
            for k, v in request.GET.items():
                params[str(k)] = v
        elif request.method == "POST":
            for k, v in request.POST.items():
                params[str(k)] = v
        handler.handle(request.method, *entities, **params)
        return HttpResponse("It works: %s!" % cmd)
    else:
        return HttpResponse('cmd %s not found' % cmd)

