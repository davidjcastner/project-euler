# Digit factorials
# Problem 34
# https://projecteuler.net/problem=34

# 145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.
# Find the sum of all numbers which are equal to the sum of the factorial of
# their digits.
# Note: As 1! = 1 and 2! = 2 are not sums they are not included.

from src.lib.calculate import factorial


def is_special(n: int, base: int = 10) -> bool:
    '''checks if n is the sum of the factorials of its digits'''
    cumulation = 0
    remainder = n
    while remainder > 0:
        cumulation += factorial(remainder % base)
        remainder = remainder // base
    return cumulation == n


def solve(limit: int = 50_000) -> str:
    '''Problem 34 - Digit factorials'''
    # original upper bound was 10_000_000 since 7 * 9! < 9_999_999
    # largest number is 40_585, so reduced upper bound for performance
    return str(sum(n for n in range(3, limit) if is_special(n)))


def test_simplified_version() -> None:
    answer = solve(limit=150)
    assert type(answer) == str
    assert answer == '145'


def test_answer() -> None:
    answer = solve()
    assert type(answer) == str
    assert answer == '40730'


if __name__ == '__main__':
    print(solve())
