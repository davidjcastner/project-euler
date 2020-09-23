# Special Pythagorean triplet
# Problem 9
# A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

# a2 + b2 = c2
# For example, 32 + 42 = 9 + 16 = 25 = 52.

# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.

from functools import reduce
import re
from typing import List


def solve() -> int:
    '''Problem 9 - Special Pythagorean triplet'''
    squares = set()
    for x in range(1, 1000):
        squares.add(x ** 2)
    for c in range(333, 1000):
        for b in range(c - 1, (c - 1) // 2, -1):
            a_squared = c ** 2 - b ** 2
            a = int(a_squared ** 0.5)
            if a_squared in squares and a + b + c == 1000:
                # print(f'{a}^2 + {b}^2 = {c}^2, {a **2} + {b**2} = {c**2}')
                return a * b * c
    return 0


if __name__ == "__main__":
    print(solve())
