from project_euler.lib.primes import is_prime


def test_normal_cases() -> None:
    assert is_prime(2) is True
    assert is_prime(3) is True
    assert is_prime(4) is False
    assert is_prime(5) is True
    assert is_prime(6) is False
    assert is_prime(7) is True
    assert is_prime(8) is False
    assert is_prime(9) is False
    assert is_prime(10) is False
    assert is_prime(11) is True
    assert is_prime(12) is False
    assert is_prime(13) is True
    assert is_prime(198) is False
    assert is_prime(199) is True
    assert is_prime(200) is False


def test_edge_cases() -> None:
    assert is_prime(-1) is False
    assert is_prime(0) is False
    assert is_prime(1) is False


def test_large_input() -> None:
    assert is_prime(198) is False
    assert is_prime(199) is True
    assert is_prime(200) is False
