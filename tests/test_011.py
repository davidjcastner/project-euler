from project_euler.solutions.s_011 import solve


def test_s_011() -> None:
    # basic example
    answer = solve(series_length=2, data_file='d_011.txt')
    assert type(answer) == str
    assert answer == str(94 * 99)

    # solve
    answer = solve()
    assert type(answer) == str
    assert answer == '70600674'
