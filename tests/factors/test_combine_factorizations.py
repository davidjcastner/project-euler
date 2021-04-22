from project_euler.lib.factors import combine_factorizations


def test_normal_cases() -> None:
    assert combine_factorizations({2: 1}, {2: 1}) == {2: 2}
    assert combine_factorizations({2: 2}, {2: 3}) == {2: 5}
    assert combine_factorizations({2: 1}, {3: 1}) == {2: 1, 3: 1}
    assert combine_factorizations({2: 1, 3: 2}, {3: 3, 5: 1}) == {2: 1, 3: 5, 5: 1}


def test_numerous_parameters() -> None:
    assert combine_factorizations({2: 1}, {3: 1}, {5: 1}, {7: 1}) == {2: 1, 3: 1, 5: 1, 7: 1}
    assert combine_factorizations({2: 2}, {3: 3}, {2: 2}, {5: 1}) == {2: 4, 3: 3, 5: 1}


def test_special_cases() -> None:
    assert combine_factorizations() == {}
    assert combine_factorizations({}) == {}
    assert combine_factorizations({}, {}, {}) == {}
    assert combine_factorizations({-1: 1}) == {-1: 1}
    assert combine_factorizations({2: 1}, {2: -1}) == {}


def test_immutability() -> None:
    # check for equivalency but not mutation
    fact_in = {}
    fact_out = combine_factorizations(fact_in)
    assert fact_in == {}
    assert fact_out == fact_in
    assert fact_in is not fact_out
    fact_in = {2: 1}
    fact_out = combine_factorizations(fact_in)
    assert fact_in == {2: 1}
    assert fact_out == fact_in
    assert fact_in is not fact_out
