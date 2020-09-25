from project_euler.solutions.s_018 import solve


def test_simplified_version() -> None:
    answer = solve(data_file='d_018.basic.txt')
    assert type(answer) == str
    assert answer == '23'


def test_answer() -> None:
    answer = solve()
    assert type(answer) == str
    assert answer == '1074'
