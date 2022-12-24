import base
from ch2 import EXPECTED, NOT_EXPECTED

EXPECTED += [
    r"get_time OK20305! (\d+)",
    "Test sleep OK20305!",
    r"current time_msec = (\d+)",
    r"time_msec = (\d+) after sleeping (\d+) ticks, delta = (\d+)ms!",
    "Test sleep1 passed20305!",
    "Test write A OK20305!",
    "Test write B OK20305!",
    "Test write C OK20305!",
]

EXPECTED += [
    "string from task info test",
    "Test task info OK20305!",
]

if __name__ == "__main__":
    base.test(EXPECTED, NOT_EXPECTED)
