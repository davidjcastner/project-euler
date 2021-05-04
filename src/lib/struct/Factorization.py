from __future__ import annotations

import math
from src.lib.utility import merge_dict


class Factorization:
    '''unique prime factorization of a positive integer'''

    def __init__(self, factors: dict[int, int] = dict()):
        assert isinstance(factors, dict)
        assert all(isinstance(base, int) for base, exp in factors.items())
        assert all(isinstance(exp, int) for base, exp in factors.items())
        assert all(base > 0 and exp > 0 for base, exp in factors.items())
        self.__factors = factors

    def __repr__(self):
        return f'Factorization({self.__factors})'

    def __hash__(self):
        # get the str representation of a dict
        # remove unnecessary whitespace and braces, leave delimiters : and ,
        # have to sort the keys first
        hashable = list(self.__factors.items())
        hashable.sort(key=lambda t: t[0])
        hashable = (f'{k}:{v}' for k, v in hashable)
        hashable = (',').join(hashable)
        return hash(hashable)

    def __eq__(self, other: Factorization):
        if not isinstance(other, Factorization):
            return False
        return self.__factors == other.__factors

    def to_dict(self) -> dict[int, int]:
        return self.__factors.copy()

    def copy(self) -> Factorization:
        return Factorization(self.__factors)

    def get_value(self) -> int:
        '''computes the value of the factorization'''
        return math.prod(base ** exp for base, exp in self.__factors.items())

    def __mul__(self, other: Factorization) -> Factorization:
        '''combines the two factorizations, result is equivalent to multiplying
        the two values of the factorizations'''
        assert isinstance(other, Factorization)
        return Factorization(
            merge_dict(lambda v1, v2: v1 + v2, self.__factors, other.__factors))

    def divisor_count(self) -> int:
        '''returns the number of divisors'''
        count = 1
        for base, exp in self.__factors.items():
            count *= exp + 1
        return count

    def exponentiate(self, exponent: int) -> int:
        '''returns the factorization of self**exponent'''
        assert isinstance(exponent, int) and exponent >= 0
        if exponent == 0:
            return Factorization({})
        new_factors = self.__factors.copy()
        for base in new_factors:
            new_factors[base] = new_factors[base] * exponent
        return Factorization(new_factors)
