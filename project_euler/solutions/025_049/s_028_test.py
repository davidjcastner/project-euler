from s_028 import solve


def test_simplified_version() -> None:
    answer = solve(n=5)
    assert type(answer) == str
    assert answer == '101'


def test_answer() -> None:
    answer = solve()
    assert type(answer) == str
    assert answer == '669171001'
