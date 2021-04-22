import pytest
from project_euler.lib.factors import proper_divisor_sum


def test_normal_cases() -> None:
    assert proper_divisor_sum(2) == sum([1])
    assert proper_divisor_sum(3) == sum([1])
    assert proper_divisor_sum(4) == sum([1, 2])
    assert proper_divisor_sum(5) == sum([1])
    assert proper_divisor_sum(6) == sum([1, 2, 3])
    assert proper_divisor_sum(7) == sum([1])
    assert proper_divisor_sum(8) == sum([1, 2, 4])
    assert proper_divisor_sum(9) == sum([1, 3])
    assert proper_divisor_sum(12) == sum([1, 2, 3, 4, 6])
    assert proper_divisor_sum(30) == sum([1, 2, 3, 5, 6, 10, 15])


def test_large_input() -> None:
    assert proper_divisor_sum(220) == sum([1, 2, 4, 5, 10, 11, 20, 22, 44, 55, 110])


def test_special_cases() -> None:
    assert proper_divisor_sum(1) == sum([1])


def test_invalid_input() -> None:
    with pytest.raises(ValueError):
        proper_divisor_sum(0)
    with pytest.raises(ValueError):
        proper_divisor_sum(-1)
    with pytest.raises(ValueError):
        proper_divisor_sum(-123456789)
