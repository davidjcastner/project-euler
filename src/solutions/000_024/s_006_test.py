from s_006 import solve


def test_simplified_version() -> None:
    answer = solve(n=10)
    assert type(answer) == str
    assert answer == '2640'


def test_answer() -> None:
    answer = solve()
    assert type(answer) == str
    assert answer == '25164150'
