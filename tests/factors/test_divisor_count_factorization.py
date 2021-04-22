from project_euler.lib.factors import divisor_count_factorization


def test_normal_cases() -> None:
    assert divisor_count_factorization({2: 1}) == 2
    assert divisor_count_factorization({3: 1}) == 2
    assert divisor_count_factorization({17: 1}) == 2
    assert divisor_count_factorization({2: 2}) == 3
    assert divisor_count_factorization({2: 3}) == 4
    assert divisor_count_factorization({2: 1, 3: 1}) == 4
    assert divisor_count_factorization({2: 1, 3: 1, 5: 1}) == 8
    assert divisor_count_factorization({2: 4, 3: 3}) == 20
    assert divisor_count_factorization({2: 3, 3: 2, 5: 1}) == 24


def test_special_cases() -> None:
    assert divisor_count_factorization({}) == 1
