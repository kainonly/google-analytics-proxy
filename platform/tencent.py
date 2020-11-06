# -*- coding: utf-8 -*-
import json
import reporting


def main_handler(event, content):
    body = json.loads(event['body'])
    result = reporting.reports(body['query'])
    return result
