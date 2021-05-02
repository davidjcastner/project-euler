# Summation of primes
# Problem 10
# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

# Find the sum of all the primes below two million.

from project_euler.lib.primes import prime_iterator


def solve(limit: int = 2 * 10 ** 6) -> str:
    '''Problem 10 - Summation of primes'''
    prime_sum = 0
    for prime in prime_iterator():
        if prime >= limit:
            break
        prime_sum += prime
    return str(prime_sum)


if __name__ == '__main__':
    print(solve())
