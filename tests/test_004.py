from project_euler.solutions.s_004 import solve


def test_s_004() -> None:
    # basic example
    answer = solve(digits=2)
    assert type(answer) == str
    assert answer == '9009'

    # solve
    answer = solve()
    assert type(answer) == str
    assert answer == '906609'
