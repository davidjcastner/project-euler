from project_euler.solutions.s_009 import solve


def test_s_009() -> None:
    # basic example
    answer = solve(triplet_sum=30)
    assert type(answer) == str
    assert answer == str(5 * 12 * 13)

    # solve
    answer = solve()
    assert type(answer) == str
    assert answer == '31875000'
