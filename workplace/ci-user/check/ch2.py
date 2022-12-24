import base

EXPECTED = [
    "Hello, world from user mode program!",
    "Test power_3 OK20305!",
    "Test power_5 OK20305!",
    "Test power_7 OK20305!",
]

TEMP = []

NOT_EXPECTED = [
    "FAIL: T.T",
]

if __name__ == "__main__":
    base.test(EXPECTED + TEMP, NOT_EXPECTED)
