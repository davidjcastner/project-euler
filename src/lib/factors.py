'''utility functions for operations related to factors/divisors'''

from src.lib.primes import nth_prime
from src.lib.struct import Factorization as Fact


class __factorization:
    '''internal cache of factorizations,

    ensures minimal calculations of factorizations'''

    __known: dict[int, Fact] = {1: Fact({})}

    @staticmethod
    def get_prime_factors(n: int, last_prime: int = 1) -> Fact:
        '''recursively calculates factorizations'''
        # check if factorization of n was already calculated
        if n in __factorization.__known:
            return __factorization.__known[n].copy()

        # get the next prime to test
        current_div = nth_prime(last_prime)

        # add the prime to factorization if not already in
        if current_div not in __factorization.__known:
            __factorization.__known[current_div] = Fact({current_div: 1})

        # can stop and conclude that n is prime if current_div ** 2 > n
        if (current_div * current_div) > n:
            fact = Fact({n: 1})
            __factorization.__known[n] = fact
            return fact

        # check if the prime divides n
        # if so, combine prime with factorization of remainder
        if n % current_div == 0:
            quotient = n // current_div
            q_fact = __factorization.get_prime_factors(quotient, last_prime)
            fact = q_fact * Fact({current_div: 1})
            __factorization.__known[n] = fact
            return fact

        # otherwise, try next prime
        else:
            return __factorization.get_prime_factors(n, last_prime + 1)


def factorize(n: int) -> Fact:
    '''returns the unique prime factorization of a positive integer'''
    assert isinstance(n, int) and n > 0
    return __factorization.get_prime_factors(n)


# def lcm_factorization(*facts: Dict[int, int]) -> Dict[int, int]:
#     '''returns the least common multiple of all factorizations input'''
#     new_factorization: Dict[int, int] = {}
#     for fact in facts:
#         for base, exponent in fact.items():
#             if base in new_factorization:
#                 new_factorization[base] = max(new_factorization[base], exponent)
#                 if new_factorization[base] == 0:
#                     del new_factorization[base]
#             else:
#                 new_factorization[base] = exponent
#     return new_factorization


# class _smart_divisor_sieve:
#     '''internal sieve for finding divisors'''

#     __sieve: List[Set[int]] = [set(), set([1]), set([1]), set([1])]

#     @staticmethod
#     def __grow_sieve() -> None:
#         '''doubles the size of the sieve'''
#         previous_length = len(_smart_divisor_sieve.__sieve)
#         for i in range(previous_length):
#             _smart_divisor_sieve.__sieve.append(set([1]))
#         sqrt = int(len(_smart_divisor_sieve.__sieve)**0.5)
#         for divisor in range(2, sqrt + 1):
#             if previous_length % divisor == 0:
#                 starting_index = previous_length
#             else:
#                 starting_index = previous_length + divisor - (previous_length % divisor)
#             for multiple in range(starting_index, len(_smart_divisor_sieve.__sieve), divisor):
#                 _smart_divisor_sieve.__sieve[multiple].add(divisor)
#                 _smart_divisor_sieve.__sieve[multiple].add(multiple // divisor)

#     @staticmethod
#     def get_divisors(n: int) -> Set[int]:
#         '''returns the set of proper divisors of n, growing the sieve as necessary'''
#         while n >= len(_smart_divisor_sieve.__sieve):
#             _smart_divisor_sieve.__grow_sieve()
#         return _smart_divisor_sieve.__sieve[n].copy()


# def proper_divisors(n: int) -> Set[int]:
#     '''returns the set of proper divisors of n'''
#     if n < 1:
#         raise ValueError
#     return _smart_divisor_sieve.get_divisors(n)


# class _smart_divisor_sums:
#     '''internal memory of divisors sum'''
#     __known_sums: Dict[int, int] = {0: 0, 1: 1}

#     @staticmethod
#     def get_sum(n: int) -> int:
#         '''returns the sum of proper divisors of n'''
#         if n not in _smart_divisor_sums.__known_sums:
#             _smart_divisor_sums.__known_sums[n] = sum(proper_divisors(n))
#         return _smart_divisor_sums.__known_sums[n]


# def proper_divisor_sum(n: int) -> int:
#     '''returns the sum of all proper divisors of n'''
#     if n < 1:
#         raise ValueError
#     return _smart_divisor_sums.get_sum(n)
