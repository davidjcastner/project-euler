from project_euler.solutions.s_025 import solve


def test_simplified_version() -> None:
    answer = solve(digits=3)
    assert type(answer) == str
    assert answer == '12'


def test_answer() -> None:
    answer = solve()
    assert type(answer) == str
    assert answer == '4782'
