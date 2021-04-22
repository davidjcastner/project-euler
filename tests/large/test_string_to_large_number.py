import pytest
from project_euler.lib.large import string_to_large_number


def test_normal_cases() -> None:
    assert string_to_large_number('1') == [1]
    assert string_to_large_number('2') == [2]
    assert string_to_large_number('3') == [3]
    assert string_to_large_number('12') == [2, 1]
    assert string_to_large_number('123456') == [6, 5, 4, 3, 2, 1]


def test_large_input() -> None:
    assert string_to_large_number('123456789000') == [0, 0, 0, 9, 8, 7, 6, 5, 4, 3, 2, 1]


def test_special_cases() -> None:
    assert string_to_large_number('') == [0]
    assert string_to_large_number('0') == [0]


def test_leading_zeros() -> None:
    assert string_to_large_number('001') == [1]
    assert string_to_large_number('000') == [0]
    assert string_to_large_number('0000123') == [3, 2, 1]


def test_invalid_input() -> None:
    with pytest.raises(ValueError):
        string_to_large_number('-1')
    with pytest.raises(ValueError):
        string_to_large_number('-123456')
    with pytest.raises(ValueError):
        string_to_large_number(' 123456')
    with pytest.raises(ValueError):
        string_to_large_number('123456 ')
    with pytest.raises(ValueError):
        string_to_large_number('123 456 ')
    with pytest.raises(ValueError):
        string_to_large_number('abc')
    with pytest.raises(ValueError):
        string_to_large_number('...')
