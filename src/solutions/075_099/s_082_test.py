from s_082 import solve


def test_simplified_version() -> None:
    answer = solve(data_file='d_082.basic.txt')
    assert type(answer) == str
    assert answer == '994'


def test_answer() -> None:
    answer = solve()
    assert type(answer) == str
    assert answer == '0'
