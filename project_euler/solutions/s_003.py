# Largest prime factor
# Problem 3
# The prime factors of 13195 are 5, 7, 13 and 29.

# What is the largest prime factor of the number 600851475143 ?

from typing import Generator, List


def primes(max_prime: int) -> Generator[int, None, None]:
    '''generates the prime numbers using a sieve'''
    is_prime = [True] * (max_prime + 1)
    is_prime[0] = False
    is_prime[1] = False
    for number in range(max_prime + 1):
        if is_prime[number]:
            for multiple in range(number ** 2, max_prime + 1, number):
                is_prime[multiple] = False
            yield number


def prime_factorization(n: int) -> List[int]:
    '''returns the prime factors of n'''
    factors = []
    max_factor = int(n ** 0.5)
    prime_gen = primes(max_factor)
    next_prime = next(prime_gen)
    while next_prime <= max_factor:
        while n % next_prime == 0:
            factors.append(next_prime)
            n = n // next_prime
            max_factor = int(n ** 0.5)
        next_prime = next(prime_gen)
    return factors + [n]


def solve() -> int:
    '''Problem 3 - Largest prime factor'''
    n = 600851475143
    return prime_factorization(600851475143)[-1]


if __name__ == "__main__":
    print(solve())
