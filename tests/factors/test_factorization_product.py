from project_euler.lib.factors import factorization_product


def test_normal_cases() -> None:
    assert factorization_product({2: 1}) == 2
    assert factorization_product({2: 2}) == 4
    assert factorization_product({2: 1, 3: 1}) == 6
    assert factorization_product({2: 1, 3: 1, 5: 1}) == 30
    assert factorization_product({5: 3, 7: 2}) == (5 ** 3 * 7 ** 2)


def test_special_cases() -> None:
    assert factorization_product({}) == 1
