from project_euler.solutions.s_005 import solve


def test_s_005() -> None:
    # basic example
    answer = solve(divisors=[range(1, 11)])
    assert type(answer) == str
    assert answer == '2520'

    # solve
    answer = solve()
    assert type(answer) == str
    assert answer == '232792560'
