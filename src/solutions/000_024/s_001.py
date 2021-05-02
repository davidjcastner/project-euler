# Multiples of 3 and 5
# Problem 1

# If we list all the natural numbers below 10 that are multiples of 3 or 5,
# we get 3, 5, 6 and 9. The sum of these multiples is 23.

# Find the sum of all the multiples of 3 or 5 below 1000.

from project_euler.lib.calculate import range_sum_int


def solve(divisor_a: int = 3, divisor_b: int = 5, range_start: int = 0, range_end: int = (1000 - 1)) -> str:
    '''Problem 1 - Multiples of 3 and 5'''
    # can be done with math:
    # sum of multiples of 3 in the range [1, 1000)
    # + sum of multiples of 5 in the range [1, 1000)
    # - sum of multiples of 15 in the range [1, 1000)
    a = range_sum_int(range_start, range_end, divisor_a)
    b = range_sum_int(range_start, range_end, divisor_b)
    c = range_sum_int(range_start, range_end, divisor_a * divisor_b)
    return str(a + b - c)


if __name__ == '__main__':
    print(solve())
