from project_euler.lib.large import large_number_sum


def test_normal_cases() -> None:
    assert large_number_sum([1], [1]) == [2]
    assert large_number_sum([1], [2]) == [3]
    assert large_number_sum([2], [3]) == [5]
    assert large_number_sum([6], [7]) == [3, 1]
    assert large_number_sum([6, 4], [7, 8]) == [3, 3, 1]
    assert large_number_sum([6, 4], [7, 8], [1, 2]) == [4, 5, 1]
    assert large_number_sum([9], [7, 8, 1, 2]) == [6, 9, 1, 2]


def test_large_input() -> None:
    large_nums = [
        [9, 8, 7, 6, 5, 4, 3, 2, 1],
        [9, 8, 7, 6, 5, 4, 3, 2, 1],
        [9, 8, 7, 6, 5, 4, 3, 2, 1],
        [9, 8, 7, 6, 5, 4, 3, 2, 1],
        [9, 8, 7, 6, 5, 4, 3, 2, 1],
        [9, 9, 9]
    ]
    assert large_number_sum(*large_nums) == [4, 4, 9, 4, 8, 2, 7, 1, 6]


def test_special_cases() -> None:
    assert large_number_sum([1]) == [1]
    assert large_number_sum([1, 2, 3]) == [1, 2, 3]
    assert large_number_sum([0]) == [0]
    assert large_number_sum([0], [0], [0]) == [0]
    assert large_number_sum([]) == [0]
    assert large_number_sum([], [], []) == [0]


def test_leading_zeros() -> None:
    assert large_number_sum([1, 0]) == [1]
    assert large_number_sum([0, 0]) == [0]
    assert large_number_sum([3, 2, 1, 0, 0, 0, 0]) == [3, 2, 1]


def test_empty_imput() -> None:
    assert large_number_sum([]) == [0]
    assert large_number_sum([], [], []) == [0]


def test_immutability() -> None:
    # check for equivalency but not mutation
    large_in = [1]
    large_out = large_number_sum(large_in)
    assert large_in == [1]
    assert large_out == large_in
    assert large_in is not large_out
    large_in = [1, 2, 3, 4]
    large_out = large_number_sum(large_in)
    assert large_in == [1, 2, 3, 4]
    assert large_out == large_in
    assert large_in is not large_out
