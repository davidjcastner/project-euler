from src.lib.primes import is_prime
from src.lib.primes import nth_prime
from src.lib.primes import prime_generator
from src.lib.primes import primes_less_than


def test_prime_generator() -> None:
    gen = prime_generator()
    assert next(gen) == 2
    assert next(gen) == 3
    assert next(gen) == 5
    assert next(gen) == 7
    assert next(gen) == 11
    assert next(gen) == 13
    assert next(gen) == 17
    assert next(gen) == 19
    assert next(gen) == 23
    assert next(gen) == 29
    assert next(gen) == 31


def test_is_prime() -> None:
    assert is_prime(-1) is False
    assert is_prime(0) is False
    assert is_prime(1) is False
    assert is_prime(2) is True
    assert is_prime(3) is True
    assert is_prime(4) is False
    assert is_prime(5) is True
    assert is_prime(6) is False
    assert is_prime(7) is True
    assert is_prime(8) is False
    assert is_prime(9) is False
    assert is_prime(10) is False
    assert is_prime(11) is True
    assert is_prime(12) is False
    assert is_prime(13) is True
    assert is_prime(198) is False
    assert is_prime(199) is True
    assert is_prime(200) is False


def test_nth_prime() -> None:
    assert nth_prime(1) == 2
    assert nth_prime(2) == 3
    assert nth_prime(3) == 5
    assert nth_prime(4) == 7
    assert nth_prime(5) == 11
    assert nth_prime(6) == 13
    assert nth_prime(7) == 17
    assert nth_prime(8) == 19
    assert nth_prime(9) == 23
    assert nth_prime(10) == 29
    assert nth_prime(1000) == 7919


def test_primes_less_than() -> None:
    assert primes_less_than(0) == []
    assert primes_less_than(1) == []
    assert primes_less_than(2) == []
    assert primes_less_than(3) == [2]
    assert primes_less_than(4) == [2, 3]
    assert primes_less_than(10) == [2, 3, 5, 7]
    assert primes_less_than(19) == [2, 3, 5, 7, 11, 13, 17]
    assert primes_less_than(20) == [2, 3, 5, 7, 11, 13, 17, 19]
