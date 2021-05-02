from __future__ import annotations

import math

# TODO: make instance of dict


class Factorization:
    '''unique prime factorization of a positive integer'''

    def __init__(self, factors: dict[int, int] = dict()):
        assert isinstance(factors, dict)
        assert all(isinstance(base, int) and isinstance(exp, int) for base, exp in factors.items())
        assert all(base > 0 and exp > 0 for base, exp in factors.items())
        self.__factors = factors

    def __repr__(self):
        return f'Factorization({self.__factors})'

    def __hash__(self):
        # get the str representation of a dict
        # remove unnecessary whitespace and braces, leave delimiters : and ,
        min_str = str(self.__factors).replace(' ', '')
        min_str = min_str.removeprefix('{').removesuffix('}')
        return hash(min_str)

    def copy(self) -> Factorization:
        return Factorization(self.__factors)

    def get_value(self) -> int:
        '''computes the value of the factorization'''
        return math.prod(base ** exp for base, exp in self.__factors.items())


if __name__ == '__main__':
    f = Factorization({2: 2, 3: 1})
    d = {f: 1}
    print(f)
    print(d)
    print(f.get_value())
