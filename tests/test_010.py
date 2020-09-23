from project_euler.solutions.s_010 import solve


def test_s_010() -> None:
    # basic example
    answer = solve(limit=10)
    assert type(answer) == str
    assert answer == '17'

    # solve
    answer = solve()
    assert type(answer) == str
    assert answer == '142913828922'
