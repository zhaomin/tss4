# Copyright (C) 2009 Software Institute, Nanjing University 

from django import template
from tss4.core_app.models import Application
import cStringIO as StringIO

register = template.Library()

@register.tag
def list_apps(parser, token):
    return AppsNode()


class AppsNode(template.Node):
    def __init__(self):
        pass

    def render(self, context):
        buf = StringIO.StringIO()
        apps = Application.objects.all()
        for app in apps:
            buf.write('<li><a href="%s" title="%s">%s</a></li>' % \
                    (app.link, app.description, app.name))
        s = buf.getvalue()
        return s

