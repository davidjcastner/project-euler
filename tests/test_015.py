from project_euler.solutions.s_015 import solve


def test_s_015() -> None:
    # basic example
    answer = solve(grid_width=2, grid_height=2)
    assert type(answer) == str
    assert answer == '6'

    # solve
    answer = solve()
    assert type(answer) == str
    assert answer == '137846528820'
