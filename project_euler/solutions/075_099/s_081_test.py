from s_081 import solve


def test_simplified_version() -> None:
    answer = solve(data_file='d_081.basic.txt')
    assert type(answer) == str
    assert answer == '2427'


def test_answer() -> None:
    answer = solve()
    assert type(answer) == str
    assert answer == '427337'
