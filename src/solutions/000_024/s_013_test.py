from s_013 import solve


def test_simplified_version() -> None:
    answer = solve(digits=5, data_file='d_013.basic.txt')
    assert type(answer) == str
    assert answer == '83484'


def test_answer() -> None:
    answer = solve()
    assert type(answer) == str
    assert answer == '5537376230'
