from project_euler.lib.primes import prime_iterator


def test_normal_cases() -> None:
    gen = prime_iterator()
    assert next(gen) == 2
    assert next(gen) == 3
    assert next(gen) == 5
    assert next(gen) == 7
    assert next(gen) == 11
    assert next(gen) == 13
    assert next(gen) == 17
    assert next(gen) == 19
    assert next(gen) == 23
    assert next(gen) == 29
    assert next(gen) == 31
