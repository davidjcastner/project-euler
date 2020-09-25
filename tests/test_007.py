from project_euler.solutions.s_007 import solve


def test_simplified_version() -> None:
    answer = solve(n=6)
    assert type(answer) == str
    assert answer == '13'


def test_answer() -> None:
    answer = solve()
    assert type(answer) == str
    assert answer == '104743'
