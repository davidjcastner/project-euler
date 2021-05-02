from src.lib.struct import Factorization


class TestFactorization:
    def test_get_value(self) -> None:
        assert Factorization({2: 2, 3: 1}) == 12
        assert Factorization({2: 3, 5: 2}) == 200
