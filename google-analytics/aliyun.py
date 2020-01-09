# -*- coding: utf-8 -*-
import json
import reporting


def handler(env, response):
    body = json.load(env['wsgi.input'])
    result = reporting.reports(body['query'])
    response("200 OK", [('Content-type', 'application/json')])
    return [json.dumps(result).encode('utf8')]
