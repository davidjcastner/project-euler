from s_012 import solve


def test_simplified_version() -> None:
    answer = solve(divisor_count=5)
    assert type(answer) == str
    assert answer == '28'


def test_answer() -> None:
    answer = solve()
    assert type(answer) == str
    assert answer == '76576500'
