from project_euler.solutions.s_014 import solve


def test_s_014() -> None:
    # basic example
    answer = solve(limit=10)
    assert type(answer) == str
    assert answer == '9'

    # solve
    answer = solve()
    assert type(answer) == str
    assert answer == '837799'
