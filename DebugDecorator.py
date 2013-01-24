#!/usr/bin/env python

from functools import wraps
from traceback import extract_stack
from inspect import isfunction


def calledfrom(signature="CallTrace", stack=0):
    def deco(func):
        @wraps(func)
        def wrapper(*args, **kw):
            trace = extract_stack()[:-1]
            print "%s: %r called from %s (line %s) in '%s': %s" % ((logsig,func.__name__,) + trace[-1])
            if stack:
                for i, e in enumerate(trace[-1:-stack-2:-1][::-1]):
                    print "%3d: %s (%s) in '%s': '%s'" % ((i,) + e)
            return func(*args, **kw)
        return wrapper
    if isfunction(signature):
        logsig = "CallStack"
        return deco(signature)
    else:
        logsig = signature
        return deco


if __name__ == "__main__":

    @calledfrom(stack=5)
    def decorated(x=1):
        print "Deko. (%s)" % x


    def stacky():
        print "Stack."
        decorated(1)
        decorated(2)

    @calledfrom("ReTrace", stack=4)
    def recursio(n):
        print "Recur(%d)" % n
        if n:
            recursio(n-1)

    recursio(4)

    class morestuff:
        @calledfrom("TestSig")
        def moremethod(self):
            print "Method."

        @calledfrom(stack=2)
        def stacktest(self):
            print "Last test."

    print "Hello."

    stacky()

    here = morestuff()
    here.moremethod()
    here.stacktest()
