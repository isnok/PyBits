#!/usr/bin/env python
# -*- coding: utf-8 -*-

from twisted.internet import reactor
from twisted.python.failure import Failure
from twisted.internet.defer import maybeDeferred
from twisted.internet.task import deferLater

def retry(result, func, args=(), kwargs={}, backoff=lambda n: 2**(n-10), maxRetries=False, tries=0, lastFailure=None):

    ''' Retry a function call. Resets tries (and therewith backoff time), if the failure changes. '''

    if isinstance(result, Failure):
        try:
            print "%r failed (%s)." % (func.__name__, result.value)
        except:
            print "Call failed (%s)." % (result.value,)

        if lastFailure is None or result.type != lastFailure.type:
            tries = 0

        lastFailure = result

    if 0 <= tries < maxRetries or maxRetries is False:
        print "Retry (%s) ..." % (tries,)
        mkNextDeferred = lambda f: maybeDeferred(f, *args, **kwargs)
        nextTry = deferLater(reactor, backoff(tries), mkNextDeferred, func)
        nextTry.addErrback(retry, func, args, kwargs, backoff, maxRetries, tries+1, lastFailure)
        return nextTry
    else:
        print "Giving up after %s unsuccesful retries (of %s)." % (tries, maxRetries)
        return result


if __name__ == "__main__":

    from random import choice

    def raiser():
        raise choice((TypeError("one"), KeyError("two")))

    dfr = retry("no_error_yet", raiser, maxRetries=3)

    dfr.addBoth(lambda _: reactor.stop())

    reactor.run()
