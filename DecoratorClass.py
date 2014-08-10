#!/usr/bin/env python

from functools import wraps
from inspect import isfunction

class Deco(object):

    def __init__(self, f_or_arg):
        print '__init__'
        if isfunction(f_or_arg):
            print 'isfunc: %s' % f_or_arg.__name__
            self.arg = None
            self.f = self.wrap(f_or_arg)
        else:
            print 'notfunc: %s' % f_or_arg.__name__
            self.arg = f_or_arg

    def wrap(self, f):
        print 'wrap', f.__name__
        @wraps(f)
        def wrapped(*args, **kwd):
            print 'wrap-'
            result = f(*args, **kwd)
            print '-ped'
            return result
        return wrapped

    def __call__(self, *args):
        print '__call__', self.arg
        if self.f:
            self.f()
        else:
            self.wrap(args[0])()


if __name__ == '__main__':
    @Deco
    def test_fun():
        print "test_fun"

    class Test(object):
        @Deco # nah...
        def fun(self):
            print 'Test.fun'

    test_fun()

    t = Test()
    t.fun()
