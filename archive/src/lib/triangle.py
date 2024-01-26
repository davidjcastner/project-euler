'''utility generators and functions related to triangle numbers'''

from typing import Generator


def nth_triangle_number(n: int) -> int:
    '''returns the nth triangle number'''
    assert isinstance(n, int) and n >= 0
    return n * (n + 1) // 2


def triangle_num_generator(n: int = 1) -> Generator[int, None, None]:
    '''generates triangle numbers, starting at the nth one'''
    assert isinstance(n, int) and n >= 0
    triangle_number = nth_triangle_number(n)
    while True:
        yield triangle_number
        n += 1
        triangle_number += n
