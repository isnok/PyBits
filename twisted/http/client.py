#!/usr/bin/env python

import sys
from twisted.python import log
log.startLogging(sys.stdout)

import twisted
log.msg("Running twisted version: %s" % twisted.__version__)

from twisted.internet import reactor
from twisted.internet.protocol import Protocol

class BodyReturner(Protocol):

    def __init__(self, finished, verbose=False):
        self.finished = finished
        self.received = ""
        self.verbose = verbose

    def dataReceived(self, bytes):
        self.received += bytes

    def connectionLost(self, reason):
        """ todo: test if reason is twisted.web.client.ResponseDone """
        if self.verbose:
            log.msg('Finished receiving body:', reason.getErrorMessage())
        self.finished.callback(self.received)

from twisted.internet.defer import Deferred

def extractReceived(response):
    d = Deferred()
    response.deliverBody(BodyReturner(d))
    return d.addCallback(logReceived)

def logReceived(content):
    log.msg("Received: %s" % content)


url = "http://localhost:3333/some/path?some=arg"


from twisted.web.client import getPage

def getPageVersion(ignored=0):
    """ this works as expected. """
    log.msg("getPage: %s" % url)
    return getPage(url).addCallback(logReceived)


from twisted.web.client import Agent

agent = Agent(reactor)

def agentVersion(ignored=0):
    """ this works as expected. """
    log.msg("Agent: %s" % url)
    return agent.request('GET', url).addCallback(extractReceived)


from cookielib import CookieJar
from twisted.web.client import CookieAgent
from twisted.web.client import HTTPConnectionPool

muffinman = CookieAgent(
        Agent(reactor, pool=HTTPConnectionPool(reactor, persistent=True)),
        CookieJar()
    )

def cookieVersion(ignored=0):
    """ this works as expected. """
    log.msg("CookieAgent: %s" % url)
    return muffinman.request('GET', url).addCallback(extractReceived)

dfr = getPageVersion()
dfr.addCallback(
        agentVersion
).addCallback(
        cookieVersion
).addBoth(
        logReceived
).addBoth(
        lambda _: reactor.stop()
)

reactor.run()
