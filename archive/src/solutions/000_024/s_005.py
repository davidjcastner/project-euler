# Smallest multiple
# Problem 5
# https://projecteuler.net/problem=5

# 2520 is the smallest number that can be divided by each of the numbers from 1
# to 10 without any remainder.

# What is the smallest positive number that is evenly divisible by all of the
# numbers from 1 to 20?

from src.lib.calculate import least_common_multiple as lcm


def solve(divisors: list[int] = list(range(1, 21))) -> str:
    '''Problem 5 - Smallest multiple'''
    return str(lcm(*divisors))


def test_simplified_version() -> None:
    answer = solve(divisors=list(range(1, 11)))
    assert type(answer) == str
    assert answer == '2520'


def test_answer() -> None:
    answer = solve()
    assert type(answer) == str
    assert answer == '232792560'


if __name__ == '__main__':
    print(solve())
