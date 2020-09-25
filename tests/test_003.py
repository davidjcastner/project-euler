from project_euler.solutions.s_003 import solve


def test_simplified_version() -> None:
    answer = solve(n=13195)
    assert type(answer) == str
    assert answer == '29'


def test_answer() -> None:
    answer = solve()
    assert type(answer) == str
    assert answer == '6857'
