from src.lib.triangle import nth_triangle_number
from src.lib.triangle import triangle_num_generator


def test_nth_triangle_number() -> None:
    assert nth_triangle_number(0) == 0
    assert nth_triangle_number(1) == 1
    assert nth_triangle_number(2) == 3
    assert nth_triangle_number(3) == 6
    assert nth_triangle_number(4) == 10
    assert nth_triangle_number(5) == 15
    assert nth_triangle_number(6) == 21
    assert nth_triangle_number(7) == 28
    assert nth_triangle_number(8) == 36


def test_triangle_num_generator() -> None:
    # standard start
    gen = triangle_num_generator()
    assert next(gen) == 1
    assert next(gen) == 3
    assert next(gen) == 6
    assert next(gen) == 10
    assert next(gen) == 15
    assert next(gen) == 21
    assert next(gen) == 28
    assert next(gen) == 36

    # start at zero
    gen = triangle_num_generator(0)
    assert next(gen) == 0
    assert next(gen) == 1
    assert next(gen) == 3
    assert next(gen) == 6
    assert next(gen) == 10
    assert next(gen) == 15
    assert next(gen) == 21

    # non standard start
    gen = triangle_num_generator(4)
    assert next(gen) == 10
    assert next(gen) == 15
    assert next(gen) == 21
    assert next(gen) == 28
    assert next(gen) == 36
    assert next(gen) == 45
    assert next(gen) == 55
    assert next(gen) == 66
    gen = triangle_num_generator(10)
    assert next(gen) == 55
    assert next(gen) == 66
