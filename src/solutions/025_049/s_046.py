# Goldbach's other conjecture
# Problem 46
# https://projecteuler.net/problem=46

# It was proposed by Christian Goldbach that every odd composite number can be
# written as the sum of a prime and twice a square.
# 9 = 7 + 2*1^2
# 15 = 7 + 2*2^2
# 21 = 3 + 2*3^2
# 25 = 7 + 2*3^2
# 27 = 19 + 2*2^2
# 33 = 31 + 2*1^2
# It turns out that the conjecture was false.
# What is the smallest odd composite that cannot be written as the sum of a
# prime and twice a square?

from src.lib.primes import is_prime
from src.lib.primes import prime_generator


class _goldbach:
    '''internal cache of goldbach numbers'''

    __prime_gen = prime_generator()
    __last_prime = 0
    __stack = []
    __known = set()

    @staticmethod
    def is_goldbach_number(n: int) -> bool:
        '''only works on odd composite numbers'''
        assert isinstance(n, int) and n > 0
        assert n % 2 == 1 and not is_prime(n)
        # first call operations
        if _goldbach.__last_prime == 0:
            next(_goldbach.__prime_gen)  # skip 2
            _goldbach.__last_prime = 2

        # check if n was already found
        if n in _goldbach.__known:
            return True

        # make sure all primes less than n add in stack
        while _goldbach.__last_prime + 2 < n:
            prime = next(_goldbach.__prime_gen)
            square = 1
            total = prime + 2
            _goldbach.__last_prime = prime
            _goldbach.__stack.append((prime, square, total))
            _goldbach.__known.add(total)
            if total == n:
                return True

        # go through each prime on stack and increment totals until greater
        # than n or n is found
        for index, (prime, square, total) in enumerate(_goldbach.__stack):
            while total < n:
                square += 1
                total = prime + 2 * square * square
                _goldbach.__known.add(total)
            _goldbach.__stack[index] = (prime, square, total)
            if total == n:
                return True
        return False


def solve() -> str:
    '''Problem 46 - Goldbach's other conjecture'''
    n = 3
    while True:
        if not is_prime(n):
            if not _goldbach.is_goldbach_number(n):
                break
        n += 2
    return str(n)


# no good simplified version
# def test_simplified_version() -> None:
#     answer = solve()
#     assert type(answer) == str
#     assert answer == '0'


def test_answer() -> None:
    answer = solve()
    assert type(answer) == str
    assert answer == '5777'


if __name__ == '__main__':
    print(solve())
