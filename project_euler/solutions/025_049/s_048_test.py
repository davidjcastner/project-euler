from s_048 import solve


def test_simplified_version() -> None:
    answer = solve(n=10, d=5)
    assert type(answer) == str
    assert answer == '71317'


def test_answer() -> None:
    answer = solve()
    assert type(answer) == str
    assert answer == '9110846700'
