from project_euler.solutions.s_020 import solve


def test_simplified_version() -> None:
    answer = solve(n=10)
    assert type(answer) == str
    assert answer == '27'


def test_answer() -> None:
    answer = solve()
    assert type(answer) == str
    assert answer == '648'
