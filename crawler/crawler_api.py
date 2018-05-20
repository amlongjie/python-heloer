# -*- coding: utf-8 -*-

import urllib2


def do_crawler(url, header=None, param=None):
    if header is None:
        header = {}
    request = urllib2.Request(url, param, header)
    return urllib2.urlopen(request, timeout=10).read()
