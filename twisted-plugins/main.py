#!/usr/bin/env python
from twisted.plugin import getPlugins
from twisted.plugin import IPlugin
from twisted.internet import reactor

from Interfaces import IMyInterface
from Interfaces import IMyOtherInterface

def findFirst():
    print "MyInterface:"
    print "============"

    for plug in getPlugins(IMyInterface):
        print plug.__name__

def findSecond():
    print "MyOtherInterface:"
    print "============"

    for plug in getPlugins(IMyOtherInterface):
        print plug.__name__

reactor.callLater(1, findFirst)
reactor.callLater(2, findSecond)
reactor.callLater(3, reactor.stop)
reactor.run()
