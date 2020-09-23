from project_euler.solutions.s_018 import solve


def test_s_018() -> None:
    # basic example
    answer = solve(data_file='./data/d_018.basic.txt')
    assert type(answer) == str
    assert answer == '23'

    # solve
    answer = solve()
    assert type(answer) == str
    assert answer == '1074'
