from project_euler.solutions.s_006 import solve


def test_s_006() -> None:
    # basic example
    answer = solve(n=10)
    assert type(answer) == str
    assert answer == '2640'

    # solve
    answer = solve()
    assert type(answer) == str
    assert answer == '25164150'
