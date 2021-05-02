from s_055 import solve


def test_simplified_version() -> None:
    answer = solve(limit=888)
    assert type(answer) == str
    assert answer == '11'


def test_answer() -> None:
    answer = solve()
    assert type(answer) == str
    assert answer == '249'
