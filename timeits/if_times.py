from collections import namedtuple

SpeedTest = namedtuple("SpeedTest", ["title", "setup", "code"])

if_tests = [
SpeedTest("if-then-else",
"""
def f(x):
    if x:
        return True
    else:
        return False
""",
""" f(0); f(1) """,
),
SpeedTest("if-fallthrough",
"""
def f(x):
    if x:
        return True
    return False
""",
""" f(0); f(1) """,
),
SpeedTest("dict-if-known-values",
"""
f = {0:False,1:True}
""",
""" f[0]; f[1] """,
),
SpeedTest("dict-if-unknown-values",
"""
f = {0:False,1:True}
""",
""" f[0]; f.get(2, True) """,
),
]
