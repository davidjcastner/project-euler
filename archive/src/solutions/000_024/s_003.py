# Largest prime factor
# Problem 3
# https://projecteuler.net/problem=3

# The prime factors of 13195 are 5, 7, 13 and 29.

# What is the largest prime factor of the number 600851475143 ?

from src.lib.factors import factorize


def solve(n: int = 600851475143) -> str:
    '''Problem 3 - Largest prime factor'''
    return str(max(factorize(n).to_dict()))


def test_simplified_version() -> None:
    answer = solve(n=13195)
    assert type(answer) == str
    assert answer == '29'


def test_answer() -> None:
    answer = solve()
    assert type(answer) == str
    assert answer == '6857'


if __name__ == '__main__':
    print(solve())
