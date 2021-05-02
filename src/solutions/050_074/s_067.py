# Maximum path sum II
# Problem 67
# https://projecteuler.net/problem=67

# By starting at the top of the triangle below and moving to adjacent numbers on
# the row below,
# the maximum total from top to bottom is 23.

# 3
# 7 4
# 2 4 6
# 8 5 9 3

# That is, 3 + 7 + 4 + 9 = 23.

# Find the maximum total from top to bottom in triangle.txt (right click and
# 'Save Link/Target As...'),
# a 15K text file containing a triangle with one-hundred rows.

# NOTE: This is a much more difficult version of Problem 18.
# It is not possible to try every route to solve this problem, as there are 299
# altogether!
# If you could check one trillion (1012) routes every second it would take over
# twenty billion years to check them all.
# There is an efficient algorithm to solve it. ;o)

from src.lib.utility import read_lines


def solve(data_file: str = 'd_067.txt') -> str:
    '''Problem 67 - Maximum path sum II'''
    data = read_lines(data_file)
    series = [[int(n) for n in line.split()] for line in data]
    for depth in range(len(series) - 2, -1, -1):
        for index in range(len(series[depth])):
            left_child_value = series[depth + 1][index]
            right_child_value = series[depth + 1][index + 1]
            series[depth][index] += max(left_child_value, right_child_value)
    return str(series[0][0])


def test_simplified_version() -> None:
    answer = solve(data_file='d_067.basic.txt')
    assert type(answer) == str
    assert answer == '23'


def test_answer() -> None:
    answer = solve()
    assert type(answer) == str
    assert answer == '7273'


if __name__ == '__main__':
    print(solve())
