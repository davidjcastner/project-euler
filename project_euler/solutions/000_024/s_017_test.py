from s_017 import solve


def test_simplified_version() -> None:
    answer = solve(n=5)
    assert type(answer) == str
    assert answer == '19'


def test_answer() -> None:
    answer = solve()
    assert type(answer) == str
    assert answer == '21124'
