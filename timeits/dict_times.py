from collections import namedtuple

SpeedTest = namedtuple("SpeedTest", ["title", "setup", "code"])

tests = [
SpeedTest("access 1-elem dict", "a={1:'x'}", "a[1]"),
SpeedTest("get from empty dict", "a={}", "x=a.get(1,'x')"),
SpeedTest("get from 1-elem dict (there)", "a={1:'x'}", "x=a.get(1,'x')"),
SpeedTest("get from 1-elem dict (not there)", "a={1:'x'}", "x=a.get(1,'x')"),
SpeedTest("if-then-else-get (in dict)",
"a={1: 'x'}",
"""
if 1 in a:
    x = a[1]
else:
    x = "x"
""",
),
SpeedTest("if-then-else-get (not in dict)",
"a={}",
"""
if 1 in a:
    x = a[1]
else:
    x = "x"
""",
),
SpeedTest("try-except working get (raw)",
"a={1:'x'}",
"""
try:
    x = a[1]
except:
    x = "x"
""",
),
SpeedTest("try-except to emulate get (raw)",
"a={}",
"""
try:
    x = a[1]
except:
    x = "x"
""",
),
SpeedTest("try-except to emulate get (specialized)",
"a={}",
"""
try:
    x = a[1]
except KeyError:
    x = "x"
""",
),
]
