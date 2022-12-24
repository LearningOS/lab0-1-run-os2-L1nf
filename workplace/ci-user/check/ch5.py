import base
from ch4 import EXPECTED, NOT_EXPECTED

EXPECTED += [
    r"Test getpid OK20305! pid = (\d+)",
    "Test spawn0 OK20305!",
    "Test wait OK20305!",
    "Test waitpid OK20305!",
    "Test set_priority OK20305!",
]

EXPECTED = list(set(EXPECTED) - set([
    "string from task info test",
    "Test task info OK20305!",
]))

TEMP = [
    # "ch5 Usertests passed20305!",
]

if __name__ == '__main__':
    base.test(EXPECTED + TEMP, NOT_EXPECTED)
