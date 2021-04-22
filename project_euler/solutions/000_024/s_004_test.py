from s_004 import solve


def test_simplified_version() -> None:
    answer = solve(digits=2)
    assert type(answer) == str
    assert answer == '9009'


def test_answer() -> None:
    answer = solve()
    assert type(answer) == str
    assert answer == '906609'
