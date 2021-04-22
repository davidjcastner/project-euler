import pytest
from project_euler.lib.factors import proper_divisors


def test_normal_cases() -> None:
    assert proper_divisors(2) == set([1])
    assert proper_divisors(3) == set([1])
    assert proper_divisors(4) == set([1, 2])
    assert proper_divisors(5) == set([1])
    assert proper_divisors(6) == set([1, 2, 3])
    assert proper_divisors(7) == set([1])
    assert proper_divisors(8) == set([1, 2, 4])
    assert proper_divisors(9) == set([1, 3])
    assert proper_divisors(12) == set([1, 2, 3, 4, 6])
    assert proper_divisors(30) == set([1, 2, 3, 5, 6, 10, 15])


def test_large_input() -> None:
    assert proper_divisors(220) == set([1, 2, 4, 5, 10, 11, 20, 22, 44, 55, 110])


def test_special_cases() -> None:
    assert proper_divisors(1) == set([1])


def test_invalid_input() -> None:
    with pytest.raises(ValueError):
        proper_divisors(0)
    with pytest.raises(ValueError):
        proper_divisors(-1)
    with pytest.raises(ValueError):
        proper_divisors(-123456789)
