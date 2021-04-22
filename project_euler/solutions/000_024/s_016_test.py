from s_016 import solve


def test_simplified_version() -> None:
    answer = solve(base=2, exponent=15)
    assert type(answer) == str
    assert answer == '26'


def test_answer() -> None:
    answer = solve()
    assert type(answer) == str
    assert answer == '1366'
