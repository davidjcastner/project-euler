from project_euler.lib.factors import lcm_factorization


def test_normal_cases() -> None:
    assert lcm_factorization({2: 1}, {2: 1}) == {2: 1}
    assert lcm_factorization({2: 2}, {2: 3}) == {2: 3}
    assert lcm_factorization({2: 1}, {3: 1}) == {2: 1, 3: 1}
    assert lcm_factorization({2: 1, 3: 2}, {3: 3, 5: 1}) == {2: 1, 3: 3, 5: 1}


def test_numerous_parameters() -> None:
    assert lcm_factorization({2: 1}, {3: 1}, {5: 1}, {7: 1}) == {2: 1, 3: 1, 5: 1, 7: 1}
    assert lcm_factorization({2: 5}, {3: 3}, {2: 2}, {5: 1}) == {2: 5, 3: 3, 5: 1}


def test_special_cases() -> None:
    assert lcm_factorization() == {}
    assert lcm_factorization({}) == {}
    assert lcm_factorization({}, {}, {}) == {}
    assert lcm_factorization({}, {11: 1}) == {11: 1}
    assert lcm_factorization({-1: 1}, {11: 1}) == {-1: 1, 11: 1}
    assert lcm_factorization({2: -1}, {2: 1}) == {2: 1}


def test_immutability() -> None:
    # check for equivalency but not mutation
    fact_in = {}
    fact_out = lcm_factorization(fact_in)
    assert fact_in == {}
    assert fact_out == fact_in
    assert fact_in is not fact_out
    fact_in = {2: 1}
    fact_out = lcm_factorization(fact_in)
    assert fact_in == {2: 1}
    assert fact_out == fact_in
    assert fact_in is not fact_out
