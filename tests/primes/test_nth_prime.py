import pytest
from project_euler.lib.primes import nth_prime


def test_normal_cases() -> None:
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


def test_large_input() -> None:
    assert nth_prime(1000) == 7919


def test_invalid_input() -> None:
    with pytest.raises(ValueError):
        nth_prime(0)
    with pytest.raises(ValueError):
        nth_prime(-1)
    with pytest.raises(ValueError):
        nth_prime(-123456789)
