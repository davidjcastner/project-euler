from src.lib.factors import factorize


def test_factorize() -> None:
    assert dict(factorize(1)) == {}
    assert dict(factorize(2)) == {2: 1}
    assert dict(factorize(3)) == {3: 1}
    assert dict(factorize(4)) == {2: 2}
    assert dict(factorize(5)) == {5: 1}
    assert dict(factorize(6)) == {2: 1, 3: 1}
    assert dict(factorize(7)) == {7: 1}
    assert dict(factorize(8)) == {2: 3}
    assert dict(factorize(9)) == {3: 2}
    assert dict(factorize(10)) == {2: 1, 5: 1}
    assert dict(factorize(11)) == {11: 1}
    assert dict(factorize(12)) == {2: 2, 3: 1}
    assert dict(factorize(3125)) == {5: 5}
    assert dict(factorize(13195)) == {5: 1, 7: 1, 13: 1, 29: 1}
    assert dict(factorize(39601)) == {199: 2}
    assert dict(factorize(1449175)) == {5: 2, 7: 3, 13: 2}
