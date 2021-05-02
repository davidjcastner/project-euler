'''shortcut formulas for fast calculations'''


def sum_range(beg: int, end: int, divisor: int = 1) -> int:
    '''returns the sum of all integers in the range [beg, end) that are
    divisible by the divisor'''
    assert isinstance(beg, int) and isinstance(end, int)
    assert beg <= end
    assert isinstance(divisor, int)
    assert divisor > 0
    calc_beg = (beg + divisor - 1) // divisor
    calc_end = end // divisor
    return ((calc_beg + calc_end) * (calc_end - calc_beg + 1) // 2) * divisor


def sum_squares(n: int) -> int:
    '''returns the sum of squares for the integers 1 to n'''
    assert isinstance(n, int) and n >= 0
    return n * (n + 1) * (2 * n + 1) // 6
