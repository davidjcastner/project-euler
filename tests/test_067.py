from project_euler.solutions.s_067 import solve


def test_s_067() -> None:
    # basic example
    answer = solve(data_file='./data/d_067.basic.txt')
    assert type(answer) == str
    assert answer == '23'

    # solve
    answer = solve()
    assert type(answer) == str
    assert answer == '7273'
