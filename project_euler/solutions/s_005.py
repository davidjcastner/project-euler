# Smallest multiple
# Problem 5
# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

from typing import Generator, Dict


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


def prime_factorization(n: int) -> Dict[int, int]:
    '''returns the prime factors of n'''
    factors: Dict[int, int] = {}
    max_factor = int(n ** 0.5)
    prime_gen = primes(max_factor)
    next_prime = next(prime_gen)
    while next_prime <= max_factor:
        while n % next_prime == 0:
            if next_prime in factors:
                factors[next_prime] += 1
            else:
                factors[next_prime] = 1
            n = n // next_prime
            max_factor = int(n ** 0.5)
        try:
            next_prime = next(prime_gen)
        except StopIteration:
            break
    if n != 1:
        if n in factors:
            factors[n] += 1
        else:
            factors[n] = 1
    return factors


def smallest_multiple_factorization(factorization_a: Dict[int, int], factorization_b: Dict[int, int]) -> Dict[int, int]:
    '''combines factorizations and returns a factorization of the smallest multiple'''
    combined_factors: Dict[int, int] = {}
    for factor, count in factorization_a.items():
        combined_factors[factor] = count
    for factor, count in factorization_b.items():
        if factor in combined_factors:
            combined_factors[factor] = max(combined_factors[factor], count)
        else:
            combined_factors[factor] = count
    return combined_factors


def unfactorize(factorization: Dict[int, int]) -> int:
    '''multiples all factors and returns the product'''
    product = 1
    for factor, count in factorization.items():
        product *= factor ** count  # type: ignore
    return product


def solve() -> int:
    '''Problem 5 - Smallest multiple'''
    factors: Dict[int, int] = {}
    for x in range(2, 20):
        factors = smallest_multiple_factorization(factors, prime_factorization(x))
    return unfactorize(factors)


if __name__ == "__main__":
    print(solve())
