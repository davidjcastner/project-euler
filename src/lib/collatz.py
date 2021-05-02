'''utility functions related to the collatz sequence'''

from typing import Generator


def next_collatz(n: int) -> int:
    '''returns the next number in the collatz sequence'''
    assert isinstance(n, int) and n >= 1
    return n // 2 if n % 2 == 0 else n * 3 + 1


def collatz_generator(n: int) -> Generator[int, None, None]:
    '''iterates through the collatz sequence from n to 1'''
    assert isinstance(n, int) and n >= 1
    while True:
        yield n
        if n == 1:
            break
        n = next_collatz(n)


class __collatz:
    '''internal cache for finding collatz length'''
    __known_lengths: dict[int, int] = {1: 0}

    @staticmethod
    def get_length(n: int) -> int:
        '''returns the length of collatz sequence of n'''
        if n in __collatz.__known_lengths:
            return __collatz.__known_lengths[n]
        length = 1 + __collatz.get_length(next_collatz(n))
        __collatz.__known_lengths[n] = length
        return length


def collatz_length(n: int) -> int:
    '''returns number of steps to get to 1'''
    assert isinstance(n, int) and n >= 1
    return __collatz.get_length(n)
