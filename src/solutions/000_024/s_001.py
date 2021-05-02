# Multiples of 3 and 5
# Problem 1
# https://projecteuler.net/problem=1

# If we list all the natural numbers below 10 that are multiples of 3 or 5,
# we get 3, 5, 6 and 9. The sum of these multiples is 23.

# Find the sum of all the multiples of 3 or 5 below 1000.

from src.lib.calculate import sum_range


def solve(
    divisor_a: int = 3,
    divisor_b: int = 5,
    range_start: int = 0,
    range_end: int = (1000 - 1)
) -> str:
    '''Problem 1 - Multiples of 3 and 5'''
    # can be done with math:
    # sum of multiples of 3 in the range [1, 1000)
    # + sum of multiples of 5 in the range [1, 1000)
    # - sum of multiples of 15 in the range [1, 1000)
    a = sum_range(range_start, range_end, divisor_a)
    b = sum_range(range_start, range_end, divisor_b)
    c = sum_range(range_start, range_end, divisor_a * divisor_b)
    return str(a + b - c)


def test_simplified_version() -> None:
    answer = solve(divisor_a=3, divisor_b=5, range_start=0, range_end=(10 - 1))
    assert type(answer) == str
    assert answer == '23'


def test_answer() -> None:
    answer = solve()
    assert type(answer) == str
    assert answer == '233168'


if __name__ == '__main__':
    print(solve())
