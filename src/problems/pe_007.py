# 10001st prime
# Problem 7
# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

# What is the 10 001st prime number?

import math
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


def nth_prime(n: int) -> int:
    '''returns the nth prime by creating a sieve with an upper bound'''
    upper_bound = int(n * math.log(n) * 1.2) + 3
    prime_gen = primes(upper_bound)
    p = next(prime_gen)
    while n > 1:
        p = next(prime_gen)
        n -= 1
    return p


def solve() -> int:
    '''Problem 7 - 10001st prime'''
    n = 10001
    return nth_prime(n)


if __name__ == "__main__":
    print(solve())
