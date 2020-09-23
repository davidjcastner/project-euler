from project_euler.solutions.s_003 import solve


def test_s_003() -> None:
    # basic example
    answer = solve(n=13195)
    assert type(answer) == str
    assert answer == '29'

    # solve
    answer = solve()
    assert type(answer) == str
    assert answer == '6857'
