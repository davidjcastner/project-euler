'''utility generators and functions related to the fibonacci sequence'''

from typing import Generator


def fibonacci_generator(a: int = 1, b: int = 1) -> Generator[int, None, None]:
    '''iterates through the fibonacci sequence using starting values'''
    assert isinstance(a, int) and isinstance(b, int)
    while True:
        yield a
        a, b = b, a + b
