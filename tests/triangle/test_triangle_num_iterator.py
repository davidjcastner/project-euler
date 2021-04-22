import pytest
from project_euler.lib.triangle import triangle_num_iterator


def test_normal_cases() -> None:
    gen = triangle_num_iterator()
    assert next(gen) == 1
    assert next(gen) == 3
    assert next(gen) == 6
    assert next(gen) == 10
    assert next(gen) == 15
    assert next(gen) == 21
    assert next(gen) == 28
    assert next(gen) == 36
    assert next(gen) == 45
    assert next(gen) == 55
    assert next(gen) == 66


def test_special_cases() -> None:
    gen = triangle_num_iterator(0)
    assert next(gen) == 0
    assert next(gen) == 1
    assert next(gen) == 3
    assert next(gen) == 6
    assert next(gen) == 10
    assert next(gen) == 15
    assert next(gen) == 21


def test_unusual_input() -> None:
    gen = triangle_num_iterator(4)
    assert next(gen) == 10
    assert next(gen) == 15
    assert next(gen) == 21
    assert next(gen) == 28
    assert next(gen) == 36
    assert next(gen) == 45
    assert next(gen) == 55
    assert next(gen) == 66
    gen = triangle_num_iterator(10)
    assert next(gen) == 55
    assert next(gen) == 66


def test_invalid_input() -> None:
    with pytest.raises(ValueError):
        for t in triangle_num_iterator(-1):
            break
    with pytest.raises(ValueError):
        for t in triangle_num_iterator(-123456789):
            break
