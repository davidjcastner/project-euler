from project_euler.solutions.s_012 import solve


def test_s_012() -> None:
    # basic example
    answer = solve(divisor_count=5)
    assert type(answer) == str
    assert answer == '28'

    # solve
    answer = solve()
    assert type(answer) == str
    assert answer == '76576500'
