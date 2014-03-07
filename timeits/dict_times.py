from collections import namedtuple

SpeedTest = namedtuple("SpeedTest", ["title", "test", "setup"])

tests = [
SpeedTest("access 1-elem dict", "a[1]", "a={1:'x'}"),
SpeedTest("get from empty dict", "x=a.get(1,'x')", "a={}"),
SpeedTest("get from 1-elem dict", "x=a.get(1,'x')", "a={1:'x'}"),
SpeedTest("try-except to emulate get (raw)",
"""
try:
    x = a[1]
except:
    x = "x"
""",
    "a={}"
),
SpeedTest("try-except to emulate get (specialized)",
"""
try:
    x = a[1]
except KeyError:
    x = "x"
""",
    "a={}"
),
]
