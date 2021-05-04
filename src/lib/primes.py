'''utility generators and functions related to primes'''

from typing import Generator


class _prime_sieve:
    '''internal sieve for prime functions'''
    # functions automatically use the sieve, and it grows automatically

    __sieve: list[bool] = [False, False, True, True]
    __prime_list: list[int] = [2, 3]

    @staticmethod
    def __extend() -> None:
        '''doubles the size of the sieve'''
        # double size of sieve's boolean values
        pre_len = len(_prime_sieve.__sieve)
        _prime_sieve.__sieve += [True] * pre_len
        # set values of known composites to false
        for prime in _prime_sieve.__prime_list:
            # calculate correct starting position based of starting index of
            # sieve extension and the current prime
            if pre_len % prime == 0:
                start = pre_len
            else:
                start = pre_len + prime - (pre_len % prime)
            # flips all multiples of current prime to False
            for multiple in range(start, len(_prime_sieve.__sieve), prime):
                _prime_sieve.__sieve[multiple] = False

    @staticmethod
    def __calculate_next_prime() -> None:
        '''finds the next prime after the last prime in prime_list,
        and adds it to prime_list'''
        # start at last known prime
        possible = _prime_sieve.__prime_list[-1]
        # continue incrementing possible prime by one until confirmed that
        # it is prime
        while True:
            possible += 1
            # extend sieve is possible prime is larger than sieve capacity
            if possible >= len(_prime_sieve.__sieve):
                _prime_sieve.__extend()
            # check sieve boolean map to see if it is prime
            if _prime_sieve.__sieve[possible]:
                # prime found, add to known prime list and until boolean sieve
                _prime_sieve.__prime_list.append(possible)
                start = possible * possible
                end = len(_prime_sieve.__sieve)
                for multiple in range(start, end, possible):
                    _prime_sieve.__sieve[multiple] = False
                break

    @staticmethod
    def is_prime(n: int) -> bool:
        '''uses the sieve to check if n is prime'''
        # continue to calculate primes until sieve's last known prime is
        # greater than or equal to n, then check boolean sieve of n
        while n > _prime_sieve.__prime_list[-1]:
            _prime_sieve.__calculate_next_prime()
        return _prime_sieve.__sieve[n]

    @staticmethod
    def nth_prime(n: int) -> int:
        '''uses the sieve's prime_list to return the nth prime'''
        # continue to calculate primes until sieve's prime list's length is
        # greater than or equal to n, then check prime list of n
        while n > len(_prime_sieve.__prime_list):
            _prime_sieve.__calculate_next_prime()
        return _prime_sieve.__prime_list[n - 1]

    @staticmethod
    def last_known_prime() -> int:
        '''exposes last known prime, useful for optimizations'''
        return _prime_sieve.__prime_list[-1]


def prime_generator() -> Generator[int, None, None]:
    '''iterates through all primes starting at 2'''
    n = 1
    while True:
        yield _prime_sieve.nth_prime(n)
        n += 1


def is_prime(n: int) -> bool:
    '''checks if n is prime'''
    assert isinstance(n, int)
    if n < 2:
        return False
    # if n is already calculated, get is_prime from sieve
    if n <= _prime_sieve.last_known_prime():
        return _prime_sieve.is_prime(n)
    # otherwise, faster to check divisibility up to the sqrt of n
    sqrt = int(n ** 0.5)
    for prime in prime_generator():
        if prime > sqrt:
            break
        if n % prime == 0:
            return False
    return True


def nth_prime(n: int) -> int:
    '''returns the nth_prime'''
    assert isinstance(n, int) and n > 0
    return _prime_sieve.nth_prime(n)
