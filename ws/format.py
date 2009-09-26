# Copyright (C) 2009 Software Institute, Nanjing University 

import simplejson as json
import cStringIO

JSON = 1
XML = 2

# TODO implement XML marshalling/unmarshalling mechanisms

def _xml_marshal_recursive(k, v, fp, enc):
    if value is None:
        fp.write('null')
    elif isinstance(value, list):
        for item in value:
            _xml_marshal_recursive(None, item, fp, enc)

def _xml_marshal(a_dict, fp, enc):
    fp.write('<?xml version="1.0" encoding="%s"?>' % enc)
    fp.write('<tss>')
    for key, value in a_dict.iteritems():
        _xml_marshal_recursive(key, value, fp, enc)
    fp.write('</tss>')

def xml_marshal(a_dict, enc="utf-8"):
    fp = cStringIO.StringIO()
    _xml_marshal(a_dict, fp, enc)
    s = fp.getvalue()
    fp.close()
    return s

def xml_unmarshal(obj):
    pass

def format_response(resp_dict, fmt=JSON):
    if fmt == JSON:
        return json.dumps(resp_dict)
    elif fmt == XML:
        return xml_marshal(resp_dict)

    return None

