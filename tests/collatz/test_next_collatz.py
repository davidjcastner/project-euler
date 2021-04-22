import pytest
from project_euler.lib.collatz import next_collatz


def test_normal_cases() -> None:
    assert next_collatz(2) == 1
    assert next_collatz(3) == 10
    assert next_collatz(4) == 2
    assert next_collatz(5) == 16
    assert next_collatz(6) == 3
    assert next_collatz(7) == 22
    assert next_collatz(8) == 4
    assert next_collatz(9) == 28
    assert next_collatz(10) == 5
    assert next_collatz(11) == 34


def test_large_input() -> None:
    assert next_collatz(1361862) == 1361862 // 2
    assert next_collatz(1361861) == 1361861 * 3 + 1


def test_special_cases() -> None:
    assert next_collatz(1) == 4


def test_invalid_input() -> None:
    with pytest.raises(ValueError):
        next_collatz(0)
    with pytest.raises(ValueError):
        next_collatz(-1)
    with pytest.raises(ValueError):
        next_collatz(-123456789)
