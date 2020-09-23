from project_euler.solutions.s_016 import solve


def test_s_016() -> None:
    # basic example
    answer = solve(base=2, exponent=15)
    assert type(answer) == str
    assert answer == '26'

    # solve
    answer = solve()
    assert type(answer) == str
    assert answer == '1366'
