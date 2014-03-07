#!/usr/bin/env python

import sys
from twisted.python import log
log.startLogging(sys.stdout)

import twisted
log.msg("Running twisted version: %s" % twisted.__version__)

from twisted.internet import reactor
from twisted.web.server import Site
from twisted.web.resource import Resource

class MyResource(Resource):
    isLeaf = True

    def render(self, request):
        log.msg("request.args is: %s" % request.args)
        return "your args were: %s" % request.args


site = Site(MyResource())
reactor.listenTCP(3333, site)

reactor.run()
