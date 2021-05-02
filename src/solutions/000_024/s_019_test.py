from s_019 import solve


def test_simplified_version() -> None:
    answer = solve(limit=1901)
    assert type(answer) == str
    assert answer == '2'


def test_answer() -> None:
    answer = solve()
    assert type(answer) == str
    assert answer == '171'
