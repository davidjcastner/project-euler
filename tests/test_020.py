from project_euler.solutions.s_020 import solve


def test_s_020() -> None:
    # basic example
    answer = solve(n=10)
    assert type(answer) == str
    assert answer == '27'

    # solve
    answer = solve()
    assert type(answer) == str
    assert answer == '648'
