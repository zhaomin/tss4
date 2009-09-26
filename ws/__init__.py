# Copyright (C) 2009 Software Institute, Nanjing University 

__all__ = ["people", ]

import inspect
from tss4.ws import format


"""
The core web service functionality of the TSS platform lies in this module.

A valid web service request is delegated to a suitable ServiceHandler. All
requests have a common URL prefix which is "service/" by default. The
trailing parts, together with other HTTP parameters, are parsed and then
passed to the ServiceHandler.handle() function.

Assuming we have a web service request to "service/user/041251023/course",
with parameters carried in POST data. The view layer will try to find the
suitable handler in ws/user.py. This is done by ws.find_handler('user').
This function locates a subclass of ServiceHandler in that module, and
calls its handle() function to process the request. handle() takes two
arguments - a list argument, entities, wrapping all URL segments after the
command (in this example, ["041251023", "course"]) in a list, and a
keyword argument, params, containing all the parameters.

Note that requests are not restricted to using HTTP POST verb only. This
means that not all requests carry parameters with them. So the kwargs
argument may be absent in some cases.
"""


class ServiceHandler:

    def handle(self, method, *entities, **params):
        """
        Handle a service and generate appropriate response.

        @param method the HTTP method of the request
        @param entities all entities specified in the URL
        @param all parameters carried by the request
        @return the response in a str
        """
        fmt = format.JSON
        if params:
            fmt = params.get('fmt', format.JSON)
        hn = getattr(self, 'handle_%s' % method)
        if hn:
            return format.format_response(hn(*entities, **params), fmt)
        else:
            return None


def find_handler(cmd):
    try:
        m = __import__('tss4.ws.%s' % cmd, {}, {}, ['ServiceHandler'])
        for k, v in m.__dict__.items():
            if inspect.isclass(v) and issubclass(v, (ServiceHandler,)) \
                    and k <> 'ServiceHandler':
                handler = v()
                return handler
    except ImportError:
        pass
    return None

