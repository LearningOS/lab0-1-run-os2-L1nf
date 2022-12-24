import base
from ch5 import EXPECTED, NOT_EXPECTED

EXPECTED += [
    "Test file0 OK20305!",
    "Test fstat OK20305!",
    "Test link OK20305!",
    "Test mass open/unlink OK20305!"
]

EXPECTED = list(set(EXPECTED) - set([
    "Test set_priority OK20305!"
]))

TEMP = [
    # "ch6 Usertests passed20305!",
]

if __name__ == '__main__':
    base.test(EXPECTED + TEMP, NOT_EXPECTED)
