# Summation of primes
# Problem 10
# https://projecteuler.net/problem=10

# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

# Find the sum of all the primes below two million.

from src.lib.primes import prime_generator


def solve(limit: int = 2 * 10 ** 6) -> str:
    '''Problem 10 - Summation of primes'''
    prime_sum = 0
    for prime in prime_generator():
        if prime >= limit:
            break
        prime_sum += prime
    return str(prime_sum)


def test_simplified_version() -> None:
    answer = solve(limit=10)
    assert type(answer) == str
    assert answer == '17'


def test_answer() -> None:
    answer = solve()
    assert type(answer) == str
    assert answer == '142913828922'


if __name__ == '__main__':
    print(solve())
