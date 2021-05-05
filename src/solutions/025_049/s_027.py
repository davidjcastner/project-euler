# Quadratic primes
# Problem 27
# https://projecteuler.net/problem=27

# Euler discovered the remarkable quadratic formula:
# n^2 + n + 41
# It turns out that the formula will produce 40 primes for the consecutive
# integer values 0 <= n <= 39. However, when n = 40,
# 40^2 + 40 + 41 = 40(40 + 1) + 41 is divisible by 41, and certainly
# when n = 41, 41^2 + 41 + 41 is clearly divisible by 41.
# The incredible formula n^2 - 79n + 1601 was discovered, which produces 80
# primes for the consecutive values 0 <= n <= 79. The product of the
# coefficients, 79 and 1601, is 126479.
# Considering quadratics of the form:

# n^2 + an + b, where |a| < 1000 and |b| <= 1000where |n| is the
# modulus/absolute value of ne.g. |11| = 11 and |-4| = 4

# Find the product of the coefficients, a and b, for the quadratic expression
# that produces the maximum number of primes for consecutive values of n,
# starting with n = 0.


from src.lib.primes import is_prime
from src.lib.primes import primes_less_than


def consecutive_primes(a: int, b: int) -> int:
    '''returns number of primes made from n^2 + an + b starting at n = 0'''
    assert isinstance(a, int) and isinstance(b, int)

    def formula(n: int) -> int:
        return n**2 + a * n + b
    n = 0
    while is_prime(formula(n)):
        n += 1
    return n


def solve(limit: int = 1000) -> str:
    '''Problem 27 - Quadratic primes'''
    # when n is even:
    # then n^2 is even, a*n is even, and b is b
    # therefore b must be odd

    # when n is odd:
    # then n^ is odd, a*n is a, and b is b
    # therefore a and b must be same sign

    # to produce consecutive primes then a and b must be odd

    # b must be greater than zero to produce positive number when n = 0
    # b must be greater than a to produce positive number when n = 1
    # b must be prime for n = 0

    # construct range of primes for b
    possible = primes_less_than(limit + 1)

    max_pair = (0, 0)  # (a,b)
    max_length = 0
    a_start = -limit + 1 if limit % 2 == 0 else -limit
    for a in range(a_start, limit + 1, 2):
        # TODO: potential optimization to find starting index of b
        for b in possible:
            if b > a:
                length = consecutive_primes(a, b)
                if length > max_length:
                    max_pair = (a, b)
                    max_length = length
    return str(max_pair[0] * max_pair[1])


def test_simplified_version() -> None:
    answer = solve(limit=41)
    assert type(answer) == str
    assert answer == '-41'


def test_answer() -> None:
    answer = solve()
    assert type(answer) == str
    assert answer == '-59231'


if __name__ == '__main__':
    print(solve())
