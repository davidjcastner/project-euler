import pytest
from project_euler.lib.factors import prime_factorization


def test_normal_cases() -> None:
    assert prime_factorization(2) == {2: 1}
    assert prime_factorization(3) == {3: 1}
    assert prime_factorization(4) == {2: 2}
    assert prime_factorization(5) == {5: 1}
    assert prime_factorization(6) == {2: 1, 3: 1}
    assert prime_factorization(7) == {7: 1}
    assert prime_factorization(8) == {2: 3}
    assert prime_factorization(9) == {3: 2}
    assert prime_factorization(10) == {2: 1, 5: 1}
    assert prime_factorization(11) == {11: 1}
    assert prime_factorization(12) == {2: 2, 3: 1}


def test_large_input() -> None:
    assert prime_factorization(199 * 199) == {199: 2}
    assert prime_factorization(13195) == {5: 1, 7: 1, 13: 1, 29: 1}
    assert prime_factorization(5**5) == {5: 5}


def test_special_cases() -> None:
    assert prime_factorization(1) == {}


def test_invalid_input() -> None:
    with pytest.raises(ValueError):
        prime_factorization(0)
    with pytest.raises(ValueError):
        prime_factorization(-1)
    with pytest.raises(ValueError):
        prime_factorization(-123456789)
