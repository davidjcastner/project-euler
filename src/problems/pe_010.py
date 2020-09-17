# Summation of primes
# Problem 10
# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

# Find the sum of all the primes below two million.

from typing import Generator


def primes(max_prime: int) -> Generator[int, None, None]:
    '''generates the prime numbers using a sieve'''
    max_prime = max(max_prime, 2)
    is_prime = [True] * (max_prime + 1)
    is_prime[0] = False
    is_prime[1] = False
    for number in range(max_prime + 1):
        if is_prime[number]:
            for multiple in range(number ** 2, max_prime + 1, number):
                is_prime[multiple] = False
            yield number


def solve() -> int:
    '''Problem 10 - Summation of primes'''
    limit = 2 * 10 ** 6
    return sum(primes(limit - 1))


if __name__ == "__main__":
    print(solve())
