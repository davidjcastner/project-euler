from project_euler.solutions.s_001 import solve


def test_s_001() -> None:
    # basic example
    answer = solve(factor_a=3, factor_b=4, range_start=0, range_end=(10 - 1))
    assert type(answer) == str
    assert answer == '233168'

    # solve
    answer = solve()
    assert type(answer) == str
    assert answer == '233168'
