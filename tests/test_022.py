from project_euler.solutions.s_022 import solve


def test_simplified_version() -> None:
    answer = solve(data_file='d_022.basic.txt')
    assert type(answer) == str
    assert answer == '64'


def test_answer() -> None:
    answer = solve()
    assert type(answer) == str
    assert answer == '871198282'
