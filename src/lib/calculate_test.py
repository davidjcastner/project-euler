from src.lib.calculate import least_common_multiple
from src.lib.calculate import sum_range
from src.lib.calculate import sum_squares


def test_sum_range() -> None:
    test_cases: tuple[int, int] = [
        (0, 0),
        (0, 1),
        (0, 2),
        (0, 3),
        (5, 11),
        (7, 31),
        (-1, 0),
        (-2, 0),
        (-3, 0),
        (-31, -7),
        (-11, 5),
        (-11, 17)
    ]
    for test_case in test_cases:
        assert sum_range(*test_case) == sum(range(*test_case))
        for divisor in range(2, 6):
            args = *test_case, divisor
            assert sum_range(args) == sum(range(args))


def test_sum_squares() -> None:
    assert sum_squares(0) == 0
    assert sum_squares(1) == 1
    assert sum_squares(2) == 5
    assert sum_squares(3) == 14
    assert sum_squares(4) == 30
    assert sum_squares(5) == 55
    assert sum_squares(10) == 385


def test_least_common_multiple() -> None:
    assert least_common_multiple() == 1
    assert least_common_multiple(1) == 1
    assert least_common_multiple(2, 3) == 6
    assert least_common_multiple(2, 3, 5) == 30
    assert least_common_multiple(4, 8) == 8
    assert least_common_multiple(2, 25, 8, 5, 10) == 200
