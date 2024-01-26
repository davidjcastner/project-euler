# Large sum
# Problem 13
# https://projecteuler.net/problem=13

# Work out the first ten digits of the sum of the following one-hundred 50-digit
# numbers.

from src.lib.utility import read_lines


def solve(digits: int = 10, data_file: str = 'd_013.txt') -> str:
    '''Problem 13 - Large sum'''
    data = read_lines(data_file)
    data = (int(n) for n in data)
    return str(sum(data))[:digits]


def test_simplified_version() -> None:
    answer = solve(digits=5, data_file='d_013.basic.txt')
    assert type(answer) == str
    assert answer == '83484'


def test_answer() -> None:
    answer = solve()
    assert type(answer) == str
    assert answer == '5537376230'


if __name__ == '__main__':
    print(solve())
