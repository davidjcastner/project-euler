from s_029 import solve


def test_simplified_version() -> None:
    answer = solve(base=range(2, 6), exponent=range(2, 6))
    assert type(answer) == str
    assert answer == '15'


def test_answer() -> None:
    answer = solve()
    assert type(answer) == str
    assert answer == '9183'
