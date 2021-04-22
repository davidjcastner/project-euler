import pytest
from project_euler.lib.triangle import nth_triangle_number


def test_normal_cases() -> None:
    assert nth_triangle_number(1) == 1
    assert nth_triangle_number(2) == 3
    assert nth_triangle_number(3) == 6
    assert nth_triangle_number(4) == 10
    assert nth_triangle_number(5) == 15
    assert nth_triangle_number(6) == 21
    assert nth_triangle_number(7) == 28
    assert nth_triangle_number(8) == 36


def test_special_cases() -> None:
    assert nth_triangle_number(0) == 0


def test_large_input() -> None:
    assert nth_triangle_number(1000) == 500500


def test_invalid_input() -> None:
    with pytest.raises(ValueError):
        nth_triangle_number(-1)
    with pytest.raises(ValueError):
        nth_triangle_number(-123456789)
