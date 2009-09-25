# Copyright (C) 2009 Software Institute, Nanjing University 

__all__ = ["tql", ]

import inspect


class ServiceHandler:
    
    def handle(request):
        """Handle the request and generate an appropriate str response.""" 
        pass


def find_handler(cmd):
    try:
        m = __import__('tss4.ws.%s' % cmd, {}, {}, ['ServiceHandler'])
        for k, v in m.__dict__.items():
            if inspect.isclass(v) and issubclass(v, (ServiceHandler,)) \
                    and k <> 'ServiceHandler':
                handler = object.__new__(v)
                handler.__init__()
                return handler
    except ImportError:
        pass
    return None

