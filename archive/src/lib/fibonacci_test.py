from src.lib.fibonacci import fibonacci_generator


def test_fibonacci_generator() -> None:
    # start from beginning
    gen = fibonacci_generator()
    assert next(gen) == 1
    assert next(gen) == 1
    assert next(gen) == 2
    assert next(gen) == 3
    assert next(gen) == 5
    assert next(gen) == 8
    assert next(gen) == 13
    assert next(gen) == 21
    assert next(gen) == 34
    assert next(gen) == 55
    assert next(gen) == 89

    # start from non standard place
    gen = fibonacci_generator(a=8, b=13)
    assert next(gen) == 8
    assert next(gen) == 13
    assert next(gen) == 21
    assert next(gen) == 34
    assert next(gen) == 55
    assert next(gen) == 89

    # generator non standard sequence
    gen = fibonacci_generator(a=8, b=-3)
    assert next(gen) == 8
    assert next(gen) == -3
    assert next(gen) == 5
    assert next(gen) == 2
    assert next(gen) == 7
    assert next(gen) == 9
    assert next(gen) == 16
