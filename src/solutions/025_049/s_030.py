# Digit fifth powers
# Problem 30
# https://projecteuler.net/problem=30

# Surprisingly there are only three numbers that can be written as the sum of
# fourth powers of their digits:
# 1634 = 1**4 + 6**4 + 3**4 + 4**4
# 8208 = 8**4 + 2**4 + 0**4 + 8**4
# 9474 = 9**4 + 4**4 + 7**4 + 4**4
# As 1 = 1**4 is not a sum it is not included.
# The sum of these numbers is 1634 + 8208 + 9474 = 19316.
# Find the sum of all the numbers that can be written as the sum of fifth
# powers of their digits.


def iter_digits(n: int, base: int = 10):
    while n > 0:
        yield n % base
        n = n // base


def digit_power_sum(n: int, power: int) -> int:
    return sum(d**power for d in iter_digits(n))


def solve(n: int = 5) -> str:
    '''Problem 30 - Digit fifth powers'''
    # not exact, but rough estimate that's definitely big enough
    limit = 10 ** (n + 1)
    result = sum(x for x in range(2, limit) if digit_power_sum(x, n) == x)
    return str(result)


if __name__ == '__main__':
    print(solve())
