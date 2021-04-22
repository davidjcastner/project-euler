from s_005 import solve


def test_simplified_version() -> None:
    answer = solve(divisors=list(range(1, 11)))
    assert type(answer) == str
    assert answer == '2520'


def test_answer() -> None:
    answer = solve()
    assert type(answer) == str
    assert answer == '232792560'
