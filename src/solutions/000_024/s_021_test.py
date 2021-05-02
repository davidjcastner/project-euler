from s_021 import solve


def test_simplified_version() -> None:
    answer = solve(limit=221)
    assert type(answer) == str
    assert answer == '220'
    answer = solve(limit=285)
    assert type(answer) == str
    assert answer == '504'


def test_answer() -> None:
    answer = solve()
    assert type(answer) == str
    assert answer == '31626'
