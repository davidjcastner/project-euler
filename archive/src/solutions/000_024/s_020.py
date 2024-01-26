# Factorial digit sum
# Problem 20
# https://projecteuler.net/problem=20

# n! means n × (n − 1) × ... × 3 × 2 × 1

# For example, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800,
# and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.

# Find the sum of the digits in the number 100!

from src.lib.calculate import factorial


def solve(n: int = 100) -> str:
    '''Problem 20 - Factorial digit sum'''
    product = factorial(n)
    digits = (int(c) for c in str(product))
    return str(sum(digits))


def test_simplified_version() -> None:
    answer = solve(n=10)
    assert type(answer) == str
    assert answer == '27'


def test_answer() -> None:
    answer = solve()
    assert type(answer) == str
    assert answer == '648'


if __name__ == '__main__':
    print(solve())
