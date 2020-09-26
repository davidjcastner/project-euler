# Amicable numbers
# Problem 21
# Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
# If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair and each of a and b are called amicable numbers.

# For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284.
# The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.

# Evaluate the sum of all the amicable numbers under 10000.

from typing import List
from valkyrie_util.factors import proper_divisors


class _divisor_sums:
    '''internal memory of divisors sum'''
    __known_sums: List[int] = [0]

    @staticmethod
    def get_sum(n: int) -> int:
        '''returns the sum of proper divisors of n'''
        current_length = len(_divisor_sums.__known_sums)
        if n >= current_length:
            _divisor_sums.__known_sums += [sum(proper_divisors(x)) for x in range(current_length, n + 1)]
        return _divisor_sums.__known_sums[n]


def solve(limit: int = 10000) -> str:
    '''Problem 21 - Amicable numbers'''
    amicable_sum = 0
    for n in range(1, limit):
        if _divisor_sums.get_sum(n) != n and _divisor_sums.get_sum(_divisor_sums.get_sum(n)) == n:
            amicable_sum += n
    return str(amicable_sum)


if __name__ == '__main__':
    print(solve())
