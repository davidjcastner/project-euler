# 10001st prime
# Problem 7
# https://projecteuler.net/problem=7

# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see
# that the 6th prime is 13.

# What is the 10 001st prime number?

from project_euler.lib.primes import nth_prime


def solve(n: int = 10001) -> str:
    '''Problem 7 - 10001st prime'''
    return str(nth_prime(n))


def test_simplified_version() -> None:
    answer = solve(n=6)
    assert type(answer) == str
    assert answer == '13'


def test_answer() -> None:
    answer = solve()
    assert type(answer) == str
    assert answer == '104743'


if __name__ == '__main__':
    print(solve())
