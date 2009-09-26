# Copyright (C) 2009 Software Institute, Nanjing University 

from tss4.ws import ServiceHandler
from tss4.ws import format

class TqlHandler(ServiceHandler):

    def handle_GET(self, *entities, **params):
        print entities
        print params
        d = {}
        return d

