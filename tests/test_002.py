from project_euler.solutions.s_002 import solve


def test_s_002() -> None:
    # basic example
    answer = solve(limit=100)
    assert type(answer) == str
    assert answer == str(2 + 8 + 34)

    # solve
    answer = solve()
    assert type(answer) == str
    assert answer == '4613732'
