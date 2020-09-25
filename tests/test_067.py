from project_euler.solutions.s_067 import solve


def test_simplified_version() -> None:
    answer = solve(data_file='./data/d_067.basic.txt')
    assert type(answer) == str
    assert answer == '23'


def test_answer() -> None:
    answer = solve()
    assert type(answer) == str
    assert answer == '7273'
