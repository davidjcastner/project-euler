# Amicable numbers
# Problem 21
# https://projecteuler.net/problem=21

# Let d(n) be defined as the sum of proper divisors of n (numbers less than n
# which divide evenly into n).
# If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair and
# each of a and b are called amicable numbers.

# For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44,
# 55 and 110; therefore d(220) = 284.
# The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.

# Evaluate the sum of all the amicable numbers under 10000.

from src.lib.factors import proper_divisor_sum


def is_amicable(n: int) -> bool:
    '''checks if n is amicable'''
    return proper_divisor_sum(n) != n and proper_divisor_sum(
        proper_divisor_sum(n)) == n


def solve(limit: int = 10000) -> str:
    '''Problem 21 - Amicable numbers'''
    return str(sum([n for n in range(1, limit) if is_amicable(n)]))


def test_simplified_version() -> None:
    answer = solve(limit=221)
    assert type(answer) == str
    assert answer == '220'
    answer = solve(limit=285)
    assert type(answer) == str
    assert answer == '504'


def test_answer() -> None:
    answer = solve()
    assert type(answer) == str
    assert answer == '31626'


if __name__ == '__main__':
    print(solve())
