import pytest
from project_euler.lib.factors import divisor_count


def test_normal_cases() -> None:
    assert divisor_count(2) == 2
    assert divisor_count(3) == 2
    assert divisor_count(17) == 2
    assert divisor_count(4) == 3
    assert divisor_count(8) == 4
    assert divisor_count(6) == 4
    assert divisor_count(30) == 8
    assert divisor_count(16 * 27) == 20
    assert divisor_count(8 * 9 * 5) == 24


def test_special_cases() -> None:
    assert divisor_count(1) == 1


def test_invalid_input() -> None:
    with pytest.raises(ValueError):
        divisor_count(0)
    with pytest.raises(ValueError):
        divisor_count(-1)
    with pytest.raises(ValueError):
        divisor_count(-123456789)
