from collections import namedtuple

SpeedTest = namedtuple("SpeedTest", ["title", "setup", "code"])

if_tests = [
SpeedTest("if-then-else",
""" """,
"""
if 0:
    True
else:
    False
if 1:
    True
else:
    False
""",
),
SpeedTest("function-if-then-else",
"""
def f(x):
    if x:
        return True
    else:
        return False
""",
""" f(0); f(1) """,
),
SpeedTest("function-if-fallthrough",
"""
def f(x):
    if x:
        return True
    return False
""",
""" f(0); f(1) """,
),
SpeedTest("dict-if-access",
"""
f = {0:False,1:True}
""",
""" f[0]; f[1] """,
),
SpeedTest("dict-if-get",
"""
f = {0:False,1:True}
""",
""" f[0]; f.get(2, True) """,
),
]
