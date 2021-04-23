from s_024 import solve


def test_simplified_version() -> None:
    answer = solve(items=set([str(x) for x in range(3)]), n=3)
    assert type(answer) == str
    assert answer == '102'
    answer = solve(items=set([str(x) for x in range(3)]), n=4)
    assert answer == '120'


def test_answer() -> None:
    answer = solve()
    assert type(answer) == str
    assert answer == '2783915460'
