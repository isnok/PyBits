#!/usr/bin/env python
"""dict speed tests

Usage:
    dict_times.py [-hrlsv] [-c N] [NUMBER ...]

Options:
    -h, --help      Show this help.
    -r, --run       Run tests. (default)
    -l, --list      List available tests. (implied if no other action)
    -s, --show      Show full tests.
    -c, --count=N   Run each test N times. [default: 1000000]
    -v, --verbose   Run and show tests.

Arguments:
    NUMBER      Run test NUMBER [default: all]
"""
from docopt import docopt
args = docopt(__doc__)

if args['--verbose'] or args['NUMBER']:
    args['--run'] = True
elif not args['--run']:
    args['--list'] = True


from collections import namedtuple

from dict_times import tests

if args['--list']:
    for i, test in enumerate(tests):
        print "%3d: %s" % (i, test.title)

def run_full(i, test):
    print "Test number %d : %s" % (i, test.title)
    print "Setup:"
    print test.setup
    print "Code:"
    print test.code
    print "Result:"
    print timeit(test.code, test.setup, number=NUMTST)
    print

def run_short(i, test):
    print "No. %d: %s ... " % (i, test.title)
    print timeit(test.code, test.setup, number=NUMTST)
    print

if args['--run']:
    from timeit import timeit
    NUMTST=int(args['--count'])

    if args['--verbose']:
        run = run_full
    else:
        run = run_short

    if not args['NUMBER']:
        for i, test in enumerate(tests):
            run(i, test)
    else:
        nums = map(int, args['NUMBER'])
        for num in nums:
            run(num, tests[num])

    print 'done.'
