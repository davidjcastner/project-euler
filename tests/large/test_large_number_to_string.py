from project_euler.lib.large import large_number_to_string


def test_normal_cases() -> None:
    assert large_number_to_string([1]) == '1'
    assert large_number_to_string([2]) == '2'
    assert large_number_to_string([3]) == '3'
    assert large_number_to_string([2, 1]) == '12'
    assert large_number_to_string([6, 5, 4, 3, 2, 1]) == '123456'


def test_large_input() -> None:
    assert large_number_to_string([0, 0, 0, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == '123456789000'


def test_special_cases() -> None:
    assert large_number_to_string([0]) == '0'
    assert large_number_to_string([]) == '0'


def test_leading_zeros() -> None:
    assert large_number_to_string([1, 0]) == '1'
    assert large_number_to_string([0, 0]) == '0'
    assert large_number_to_string([3, 2, 1, 0, 0, 0, 0]) == '123'
