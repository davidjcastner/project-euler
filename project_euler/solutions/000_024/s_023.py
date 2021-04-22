# Non-abundant sums
# Problem 23
# A perfect number is a number for which the sum of its proper divisors is exactly equal to the number.
# For example, the sum of the proper divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28,
# which means that 28 is a perfect number.

# A number n is called deficient if the sum of its proper divisors is less than n
# and it is called abundant if this sum exceeds n.

# As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16,
# the smallest number that can be written as the sum of two abundant numbers is 24.
# By mathematical analysis, it can be shown that all integers greater than
# 28123 can be written as the sum of two abundant numbers.
# However, this upper limit cannot be reduced any further by analysis
# even though it is known that the greatest number that cannot
# be expressed as the sum of two abundant numbers is less than this limit.

# Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.

import itertools
from project_euler.lib.factors import proper_divisor_sum


def is_abundant(n: int) -> bool:
    '''checks if a number is abundant'''
    return proper_divisor_sum(n) > n


def solve(limit: int = 28123) -> str:
    '''Problem 23 - Non-abundant sums'''
    abundant_numbers = [n for n in range(1, limit + 1) if is_abundant(n)]
    possible_sums = set(sum(t) for t in itertools.combinations_with_replacement(abundant_numbers, 2))
    return str(sum(n for n in range(1, limit + 1) if n not in possible_sums))


if __name__ == '__main__':
    print(solve())
