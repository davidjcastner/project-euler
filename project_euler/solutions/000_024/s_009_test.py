from s_009 import solve


def test_simplified_version() -> None:
    answer = solve(triplet_sum=30)
    assert type(answer) == str
    assert answer == str(5 * 12 * 13)


def test_answer() -> None:
    answer = solve()
    assert type(answer) == str
    assert answer == '31875000'
