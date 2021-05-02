from s_030 import solve


def test_simplified_version() -> None:
    answer = solve(n=4)
    assert type(answer) == str
    assert answer == '19316'


def test_answer() -> None:
    answer = solve()
    assert type(answer) == str
    assert answer == '443839'
