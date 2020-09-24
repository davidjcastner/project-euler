from project_euler.solutions.s_008 import solve


def test_s_008() -> None:
    # basic example
    answer = solve(factor_count=4, data_file='d_008.txt')
    assert type(answer) == str
    assert answer == '5832'

    # solve
    answer = solve()
    assert type(answer) == str
    assert answer == '23514624000'
