# Largest prime factor
# Problem 3
# The prime factors of 13195 are 5, 7, 13 and 29.

# What is the largest prime factor of the number 600851475143 ?

from valkyrie_util.factors import prime_factorization


def solve(n: int = 600851475143) -> str:
    '''Problem 3 - Largest prime factor'''
    return str(max(prime_factorization(n)))


if __name__ == '__main__':
    print(solve())
