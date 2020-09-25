from project_euler.solutions.s_015 import solve


def test_simplified_version() -> None:
    answer = solve(grid_width=2, grid_height=2)
    assert type(answer) == str
    assert answer == '6'


def test_answer() -> None:
    answer = solve()
    assert type(answer) == str
    assert answer == '137846528820'
