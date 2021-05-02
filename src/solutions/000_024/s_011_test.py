from s_011 import solve


def test_simplified_version() -> None:
    answer = solve(series_length=2, data_file='d_011.txt')
    assert type(answer) == str
    assert answer == str(97 * 99)


def test_answer() -> None:
    answer = solve()
    assert type(answer) == str
    assert answer == '70600674'
