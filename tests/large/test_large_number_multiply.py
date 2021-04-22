import pytest
from project_euler.lib.large import large_number_multiply


def test_normal_cases() -> None:
    assert large_number_multiply([1], 2) == [2]
    assert large_number_multiply([2], 2) == [4]
    assert large_number_multiply([3], 2) == [6]
    assert large_number_multiply([3], 4) == [2, 1]
    assert large_number_multiply([9, 9], 9) == [1, 9, 8]
    assert large_number_multiply([6, 7], 12) == [2, 1, 9]


def test_large_input() -> None:
    assert large_number_multiply([6, 5, 4, 3, 2, 1], 789) == [4, 8, 7, 6, 0, 4, 7, 9]


def test_special_cases() -> None:
    assert large_number_multiply([1], 1) == [1]
    assert large_number_multiply([0], 1) == [0]
    assert large_number_multiply([0], 123456789) == [0]
    assert large_number_multiply([1], 0) == [0]
    assert large_number_multiply([2], 0) == [0]
    assert large_number_multiply([3], 0) == [0]
    assert large_number_multiply([1, 2, 3, 4, 5, 6], 0) == [0]


def test_leading_zeros() -> None:
    assert large_number_multiply([1, 0], 1) == [1]
    assert large_number_multiply([3, 0], 2) == [6]
    assert large_number_multiply([3, 0, 0, 0], 4) == [2, 1]


def test_empty_imput() -> None:
    assert large_number_multiply([], 1) == [0]
    assert large_number_multiply([], 2) == [0]
    assert large_number_multiply([], 4) == [0]


def test_immutability() -> None:
    # check for equivalency but not mutation
    large_in = [1]
    large_out = large_number_multiply(large_in, 1)
    assert large_in == [1]
    assert large_out == large_in
    assert large_in is not large_out
    large_in = [1, 2, 3, 4]
    large_out = large_number_multiply(large_in, 1)
    assert large_in == [1, 2, 3, 4]
    assert large_out == large_in
    assert large_in is not large_out


def test_invalid_input() -> None:
    with pytest.raises(ValueError):
        large_number_multiply([], -1)
    with pytest.raises(ValueError):
        large_number_multiply([], -123456)
