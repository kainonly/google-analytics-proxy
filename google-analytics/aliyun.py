# -*- coding: utf-8 -*-
import json
import reporting


def handler(event, context):
    param = json.loads(event)
    body = reporting.reports(param['query'])
    context("200 OK", [('Content-type', 'application/json')])
    return [json.dumps(body).encode('utf8')]
