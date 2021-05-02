from s_023 import solve


def test_simplified_version() -> None:
    answer = solve(limit=24)
    assert type(answer) == str
    assert answer == str(sum(range(24)))


def test_answer() -> None:
    answer = solve()
    assert type(answer) == str
    assert answer == '4179871'
