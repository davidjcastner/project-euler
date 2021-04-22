import pytest
from project_euler.lib.collatz import collatz_length


def test_normal_cases() -> None:
    assert collatz_length(2) == 2
    assert collatz_length(3) == 8
    assert collatz_length(4) == 3
    assert collatz_length(5) == 6
    assert collatz_length(6) == 9
    assert collatz_length(8) == 4
    assert collatz_length(10) == 7


def test_large_input() -> None:
    assert collatz_length(27) == 112


def test_special_cases() -> None:
    assert collatz_length(1) == 1


def test_invalid_input() -> None:
    with pytest.raises(ValueError):
        collatz_length(0)
    with pytest.raises(ValueError):
        collatz_length(-1)
    with pytest.raises(ValueError):
        collatz_length(-123456789)
