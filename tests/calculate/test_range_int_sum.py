from project_euler.lib.calculate import range_sum_int


def test_normal_cases() -> None:
    assert range_sum_int(0, 0) == 0
    assert range_sum_int(0, 1) == 1
    assert range_sum_int(0, 2) == 3
    assert range_sum_int(0, 3) == 6
    assert range_sum_int(1, 0) == 1
    assert range_sum_int(2, 0) == 3
    assert range_sum_int(3, 0) == 6
    assert range_sum_int(5, 6) == 11


def test_edge_cases() -> None:
    assert range_sum_int(0, 11, 4) == 12
    assert range_sum_int(0, 12, 4) == 24
    assert range_sum_int(0, 13, 4) == 24
    assert range_sum_int(3, 11, 4) == 12
    assert range_sum_int(3, 12, 4) == 24
    assert range_sum_int(3, 13, 4) == 24
    assert range_sum_int(4, 11, 4) == 12
    assert range_sum_int(4, 12, 4) == 24
    assert range_sum_int(4, 13, 4) == 24
    assert range_sum_int(5, 11, 4) == 8
    assert range_sum_int(5, 12, 4) == 20
    assert range_sum_int(5, 13, 4) == 20
