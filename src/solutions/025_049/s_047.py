# Distinct primes factors
# Problem 47
# https://projecteuler.net/problem=47

# The first two consecutive numbers to have two distinct prime factors are:
# 14 = 2 * 7
# 15 = 3 * 5
# The first three consecutive numbers to have three distinct prime factors are:
# 644 = 2**2 * 7 * 23
# 645 = 3 * 5 * 43
# 646 = 2 * 17 * 19.
# Find the first four consecutive integers to have four distinct prime factors
# each. What is the first of these numbers?

from src.lib.factors import factorize


def solve(n: int = 4) -> str:
    '''Problem 47 - Distinct primes factors'''
    current = 2
    count = 0
    first_num = 0
    while count < n:
        distinct_primes = factorize(current).distinct_factors()
        if distinct_primes == n:
            if count == 0:
                first_num = current
            count += 1
        else:
            count = 0
        current += 1
    return str(first_num)


def test_simplified_version() -> None:
    answer = solve(3)
    assert type(answer) == str
    assert answer == '644'


def test_answer() -> None:
    answer = solve()
    assert type(answer) == str
    assert answer == '134043'


if __name__ == '__main__':
    print(solve())
