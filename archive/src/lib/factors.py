'''utility functions for operations related to factors/divisors'''

from src.lib.primes import nth_prime
from src.lib.struct.Factorization import Factorization as Fact


class _factorization:
    '''internal cache of factorizations,

    ensures minimal calculations of factorizations'''

    __known: dict[int, Fact] = {1: Fact({})}

    @staticmethod
    def get_prime_factors(n: int, last_prime: int = 1) -> Fact:
        '''recursively calculates factorizations'''
        # check if factorization of n was already calculated
        if n in _factorization.__known:
            return _factorization.__known[n].copy()

        # get the next prime to test
        current_div = nth_prime(last_prime)

        # add the prime to factorization if not already in
        if current_div not in _factorization.__known:
            _factorization.__known[current_div] = Fact({current_div: 1})

        # can stop and conclude that n is prime if current_div ** 2 > n
        if (current_div * current_div) > n:
            fact = Fact({n: 1})
            _factorization.__known[n] = fact
            return fact

        # check if the prime divides n
        # if so, combine prime with factorization of remainder
        if n % current_div == 0:
            quotient = n // current_div
            q_fact = _factorization.get_prime_factors(quotient, last_prime)
            fact = q_fact * Fact({current_div: 1})
            _factorization.__known[n] = fact
            return fact

        # otherwise, try next prime
        else:
            return _factorization.get_prime_factors(n, last_prime + 1)


def factorize(n: int) -> Fact:
    '''returns the unique prime factorization of a positive integer'''
    assert isinstance(n, int) and n > 0
    return _factorization.get_prime_factors(n)


class _divisor_sieve:
    '''internal sieve for finding proper divisors'''

    __sieve: list[set[int]] = [set(), set([1]), set([1]), set([1])]

    @staticmethod
    def __extend() -> None:
        '''doubles the size of the sieve'''
        # initialize sets for divisors for extended section
        pre_len = len(_divisor_sieve.__sieve)
        for i in range(pre_len):
            _divisor_sieve.__sieve.append(set([1]))
        # check divisors up to sqrt of max len
        sqrt = int(len(_divisor_sieve.__sieve)**0.5)
        for divisor in range(2, sqrt + 1):
            # find the next multiple of divisor that is >= section start
            if pre_len % divisor == 0:
                start = pre_len
            else:
                start = pre_len + divisor - (pre_len % divisor)
            # add divisor to all multiples
            for multiple in range(start, len(_divisor_sieve.__sieve), divisor):
                _divisor_sieve.__sieve[multiple].add(divisor)
                _divisor_sieve.__sieve[multiple].add(multiple // divisor)

    @staticmethod
    def get_divisors(n: int) -> set[int]:
        '''returns the set of proper divisors of n,
        growing the sieve as necessary'''
        while n >= len(_divisor_sieve.__sieve):
            _divisor_sieve.__extend()
        return _divisor_sieve.__sieve[n].copy()


def proper_divisors(n: int) -> set[int]:
    '''returns the set of proper divisors of a positive integer'''
    assert isinstance(n, int) and n > 0
    return _divisor_sieve.get_divisors(n)


class _divisor_sums:
    '''internal cache of divisors sum'''
    __known: dict[int, int] = {0: 0, 1: 1}

    @staticmethod
    def get_sum(n: int) -> int:
        '''returns the sum of proper divisors of n'''
        if n not in _divisor_sums.__known:
            _divisor_sums.__known[n] = sum(proper_divisors(n))
        return _divisor_sums.__known[n]


def proper_divisor_sum(n: int) -> int:
    '''returns the sum of all proper divisors of a positive integer'''
    assert isinstance(n, int) and n > 0
    return _divisor_sums.get_sum(n)
