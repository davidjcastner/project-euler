# Smallest multiple
# Problem 5
# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

from typing import List
from valkyrie_util.factors import factorization_product, lcm_factorization, prime_factorization


def solve(divisors: List[int] = list(range(1, 21))) -> str:
    '''Problem 5 - Smallest multiple'''
    prime_facts = [prime_factorization(d) for d in divisors]
    return str(factorization_product(lcm_factorization(prime_facts)))


if __name__ == '__main__':
    print(solve())
