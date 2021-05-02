import pytest
from src.lib.collatz import next_collatz
from src.lib.collatz import collatz_generator
from src.lib.collatz import collatz_length


def test_next_collatz() -> None:
    assert next_collatz(1) == 4
    assert next_collatz(2) == 1
    assert next_collatz(3) == 10
    assert next_collatz(4) == 2
    assert next_collatz(5) == 16
    assert next_collatz(6) == 3
    assert next_collatz(7) == 22
    assert next_collatz(8) == 4
    assert next_collatz(9) == 28
    assert next_collatz(10) == 5
    assert next_collatz(11) == 34
    assert next_collatz(1361862) == 1361862 // 2
    assert next_collatz(1361861) == 1361861 * 3 + 1


def test_collatz_generator() -> None:
    # normal input
    gen = collatz_generator(13)
    assert next(gen) == 13
    assert next(gen) == 40
    assert next(gen) == 20
    assert next(gen) == 10
    assert next(gen) == 5
    assert next(gen) == 16
    assert next(gen) == 8
    assert next(gen) == 4

    # large input
    gen = collatz_generator(1361862)
    assert next(gen) == 1361862
    assert next(gen) == 1361862 // 2
    gen = collatz_generator(1361861)
    assert next(gen) == 1361861
    assert next(gen) == 1361861 * 3 + 1

    # stop generator
    gen = collatz_generator(2)
    assert next(gen) == 2
    assert next(gen) == 1
    with pytest.raises(StopIteration):
        next(gen)


def test_collatz_length() -> None:
    assert collatz_length(1) == 0
    assert collatz_length(2) == 1
    assert collatz_length(3) == 7
    assert collatz_length(4) == 2
    assert collatz_length(5) == 5
    assert collatz_length(6) == 8
    assert collatz_length(8) == 3
    assert collatz_length(10) == 6
    assert collatz_length(27) == 111
