from project_euler.solutions.s_007 import solve


def test_s_007() -> None:
    # basic example
    answer = solve(n=6)
    assert type(answer) == str
    assert answer == '13'

    # solve
    answer = solve()
    assert type(answer) == str
    assert answer == '104743'
