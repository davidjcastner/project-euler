from src.lib.struct import Factorization


class TestFactorization:
    def test_get_value(self) -> None:
        assert Factorization({2: 2, 3: 1}) == 12
        assert Factorization({2: 3, 5: 2}) == 200

    def test_mul(self) -> None:
        # test cases are in the form of (a, b, c)
        # where a and b are the factors in the multiplication
        # and c is the expected result
        test_cases = [
            ({}, {}, {}),
            ({2: 1}, {}, {2: 1}),
            ({5: 3, 7: 4}, {}, {5: 3, 7: 4}),
            ({5: 3, 7: 4}, {2: 3}, {2: 3, 5: 3, 7: 4}),
            ({5: 3, 7: 4}, {2: 3, 5: 2}, {2: 3, 5: 5, 7: 4})
        ]
        for a, b, c in test_cases:
            result = Factorization(a) * Factorization(b)
            expected = Factorization(c)
            assert result == expected

    def test_divisor_count() -> None:
        assert Factorization({}).divisor_count() == 1
        assert Factorization({2: 1}).divisor_count() == 2
        assert Factorization({2: 1, 3: 1}).divisor_count() == 4
        assert Factorization({2: 3, 3: 2, 5: 2}).divisor_count() == 36

    def test_exponentiate() -> None:
        # test cases are in the form of (a, b, c)
        # where a is the input factorization
        # b is the exponent
        # c is the expected result
        test_cases = [
            ({}, 0, {}),
            ({}, 1, {}),
            ({}, 2, {}),
            ({}, 3, {}),
            ({2: 1}, 3, {2: 3}),
            ({3: 5, 5: 2}, 0, {}),
            ({2: 3, 7: 4}, 5, {2: 15, 7: 20})
        ]
        for a, b, c in test_cases:
            assert Factorization(a).exponentiate(b) == Factorization(c)
