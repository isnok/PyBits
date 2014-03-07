#!/usr/bin/env python
"""dict speed tests

Usage:
    dict_times.py [-hrlsv] [-c N] [NUMBER ...]

Options:
    -h, --help      Show this help.
    -r, --run       Run tests. (default)
    -l, --list      List available tests.
    -s, --show      Show full tests.
    -c, --count=N   Run each test N times. [default: 1000000]
    -v, --verbose   Run and show tests.

Arguments:
    NUMBER      Run test NUMBER [default: all]
"""
from docopt import docopt
args = docopt(__doc__)

if args['--verbose']:
    args['--run'] = True
    #print args

if args['NUMBER'] is None:
    args['NUMBER'] = "all"

from collections import namedtuple

from dict_times import tests

print "starting up..."

if args['--list']:
    for i, test in enumerate(tests):
        print "%3d: %s" % (i, test.title)

def run_full(i, test):
    print "Test number %d - %s" % (i, test.title)
    print "Setup:"
    print test.setup
    print "Code:"
    print test.test
    print "Result:"
    print timeit(test.test, test.setup, number=NUMTST)
    print

def run_short(i, test):
    print "No. %d: %s ... " % (i, test.title)
    print timeit(test.test, test.setup, number=NUMTST)
    print

if args['--run']:
    from timeit import timeit
    NUMTST=int(args['--count'])
    if args['--verbose']:
        for i, test in enumerate(tests):
            run_full(i, test)
    else:
        for i, test in enumerate(tests):
            run_short(i, test)

print 'done.'
