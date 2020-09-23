from project_euler.solutions.s_013 import solve


def test_s_013() -> None:
    # no basic example

    # solve
    answer = solve()
    assert type(answer) == str
    assert answer == '5537376230'
