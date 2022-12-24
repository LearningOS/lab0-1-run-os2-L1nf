import base
from ch5 import NOT_EXPECTED

EXPECTED = [
    # ch2b
    "Hello, world from user mode program!",
    "Test power_3 OK20305!",
    "Test power_5 OK20305!",
    "Test power_7 OK20305!",
    # ch3b
    r"get_time OK20305! (\d+)",
    "Test sleep OK20305!",
    r"current time_msec = (\d+)",
    r"time_msec = (\d+) after sleeping (\d+) ticks, delta = (\d+)ms!",
    "Test sleep1 passed20305!",
    "Test write A OK20305!",
    "Test write B OK20305!",
    "Test write C OK20305!",
    # ch5b
    "forktest2 test passed20305!",
    # ch6b
    "file_test passed20305!",
    # ch7b
    "pipetest passed20305!",
    # ch8b
    "mpsc_sem passed20305!",
    "philosopher dining problem with mutex test passed20305!",
    "race adder using spin mutex test passed20305!",
    "sync_sem passed20305!",
    "test_condvar passed20305!",
    "threads with arg test passed20305!",
    "threads test passed20305!",
    # ch8
    "deadlock test mutex 1 OK20305!",
    "deadlock test semaphore 1 OK20305!",
    "deadlock test semaphore 2 OK20305!",
    "ch8 Usertests passed20305!",
]


if __name__ == "__main__":
    base.test(EXPECTED, NOT_EXPECTED)
