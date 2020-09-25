from project_euler.solutions.s_010 import solve


def test_simplified_version() -> None:
    answer = solve(limit=10)
    assert type(answer) == str
    assert answer == '17'


def test_answer() -> None:
    answer = solve()
    assert type(answer) == str
    assert answer == '142913828922'
