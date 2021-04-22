import pytest
from project_euler.lib.collatz import collatz_iterator


def test_normal_cases() -> None:
    gen = collatz_iterator(13)
    assert next(gen) == 13
    assert next(gen) == 40
    assert next(gen) == 20
    assert next(gen) == 10
    assert next(gen) == 5
    assert next(gen) == 16
    assert next(gen) == 8
    assert next(gen) == 4


def test_large_input() -> None:
    gen = collatz_iterator(1361862)
    assert next(gen) == 1361862
    assert next(gen) == 1361862 // 2
    gen = collatz_iterator(1361861)
    assert next(gen) == 1361861
    assert next(gen) == 1361861 * 3 + 1


def test_stop_iteration() -> None:
    gen = collatz_iterator(2)
    assert next(gen) == 2
    assert next(gen) == 1
    with pytest.raises(StopIteration):
        next(gen)


def test_invalid_input() -> None:
    with pytest.raises(ValueError):
        next(collatz_iterator(0))
    with pytest.raises(ValueError):
        next(collatz_iterator(-1))
    with pytest.raises(ValueError):
        next(collatz_iterator(-123456789))
