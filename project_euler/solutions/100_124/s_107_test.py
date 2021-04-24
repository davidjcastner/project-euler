from s_107 import solve


def test_simplified_version() -> None:
    answer = solve(data_file='d_107.basic.txt')
    assert type(answer) == str
    assert answer == '150'


def test_answer() -> None:
    answer = solve()
    assert type(answer) == str
    assert answer == '259679'
