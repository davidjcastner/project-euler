from src.lib.factors import factorize
from src.lib.factors import proper_divisors
from src.lib.factors import proper_divisor_sum


def test_factorize() -> None:
    assert factorize(1).to_dict() == {}
    assert factorize(2).to_dict() == {2: 1}
    assert factorize(3).to_dict() == {3: 1}
    assert factorize(4).to_dict() == {2: 2}
    assert factorize(5).to_dict() == {5: 1}
    assert factorize(6).to_dict() == {2: 1, 3: 1}
    assert factorize(7).to_dict() == {7: 1}
    assert factorize(8).to_dict() == {2: 3}
    assert factorize(9).to_dict() == {3: 2}
    assert factorize(10).to_dict() == {2: 1, 5: 1}
    assert factorize(11).to_dict() == {11: 1}
    assert factorize(12).to_dict() == {2: 2, 3: 1}
    assert factorize(3125).to_dict() == {5: 5}
    assert factorize(13195).to_dict() == {5: 1, 7: 1, 13: 1, 29: 1}
    assert factorize(39601).to_dict() == {199: 2}
    assert factorize(1449175).to_dict() == {5: 2, 7: 3, 13: 2}


def test_proper_divisors() -> None:
    assert proper_divisors(1) == set([1])
    assert proper_divisors(2) == set([1])
    assert proper_divisors(3) == set([1])
    assert proper_divisors(4) == set([1, 2])
    assert proper_divisors(5) == set([1])
    assert proper_divisors(6) == set([1, 2, 3])
    assert proper_divisors(7) == set([1])
    assert proper_divisors(8) == set([1, 2, 4])
    assert proper_divisors(9) == set([1, 3])
    assert proper_divisors(12) == set([1, 2, 3, 4, 6])
    assert proper_divisors(30) == set([1, 2, 3, 5, 6, 10, 15])


def test_proper_divisor_sum() -> None:
    assert proper_divisor_sum(1) == sum([1])
    assert proper_divisor_sum(2) == sum([1])
    assert proper_divisor_sum(3) == sum([1])
    assert proper_divisor_sum(4) == sum([1, 2])
    assert proper_divisor_sum(5) == sum([1])
    assert proper_divisor_sum(6) == sum([1, 2, 3])
    assert proper_divisor_sum(7) == sum([1])
    assert proper_divisor_sum(8) == sum([1, 2, 4])
    assert proper_divisor_sum(9) == sum([1, 3])
    assert proper_divisor_sum(12) == sum([1, 2, 3, 4, 6])
    assert proper_divisor_sum(30) == sum([1, 2, 3, 5, 6, 10, 15])
    assert proper_divisor_sum(220) == 284
