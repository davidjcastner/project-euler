'''shortcut formulas for fast calculations'''

from functools import cache
from src.lib.struct import Factorization
from src.lib.factors import factorize
from src.lib.utility import merge_dict


def sum_range(beg: int, end: int, divisor: int = 1) -> int:
    '''returns the sum of all integers in the range [beg, end) that are
    divisible by the divisor'''
    assert isinstance(beg, int) and isinstance(end, int)
    assert beg <= end
    assert isinstance(divisor, int)
    assert divisor > 0
    calc_beg = (beg + divisor - 1) // divisor
    calc_end = (end - 1) // divisor
    return ((calc_beg + calc_end) * (calc_end - calc_beg + 1) // 2) * divisor


def sum_squares(n: int) -> int:
    '''returns the sum of squares for the integers 1 to n'''
    assert isinstance(n, int) and n >= 0
    return n * (n + 1) * (2 * n + 1) // 6


@cache
def factorial(n: int) -> int:
    '''returns n! for integers >= 0'''
    assert isinstance(n, int) and n >= 0
    return n * factorial(n - 1) if n > 1 else 1


def least_common_multiple(*args: tuple[int]) -> int:
    '''returns the least common multiple for all positive integers given'''
    assert all(isinstance(n, int) and n > 0 for n in args)
    # lcm can be found by combining factorizations and taking max of overlap
    fact = Factorization(merge_dict(max, *(dict(factorize(n)) for n in args)))
    return fact.get_value()
