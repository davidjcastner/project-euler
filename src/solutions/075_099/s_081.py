# Path sum: two ways
# Problem 81
# https://projecteuler.net/problem=81

# In the 5 by 5 matrix below, the minimal path sum from the top left to the
# bottom right, by only moving to the right and down, is indicated in bold red
# and is equal to 2427.

# 131 673 234 103  18
# 201  96 342 965 150
# 630 803 746 422 111
# 537 699 497 121 956
# 805 732 524  37 331

# Find the minimal path sum from the top left to the bottom right by only moving
# right and down in matrix.txt (right click and "Save Link/Target As..."), a
# 31K text file containing an 80 by 80 matrix.

from src.lib.struct import Matrix
from src.lib.utility import read_matrix


def find_min_path(m: Matrix) -> int:
    '''finds the min path in the matrix from top left to bottom right,
    only uses down and right directions for pathing'''
    min_values = m.blank_copy()
    for row, col in m.iter_rows_cols(reverse=True):
        node_value = m[m.get_index(row, col)]
        min_path = 0
        if row + 1 == m.rows and col + 1 == m.cols:
            min_path = node_value
        elif row + 1 == m.rows:
            min_path = node_value + min_values[m.get_index(
                row=row, col=col + 1)]
        elif col + 1 == m.cols:
            min_path = node_value + min_values[m.get_index(
                row=row + 1, col=col)]
        else:
            min_path = node_value + min(
                min_values[m.get_index(row=row, col=col + 1)],
                min_values[m.get_index(row=row + 1, col=col)])
        min_values[m.get_index(row, col)] = min_path
    return min_values.get(row=0, col=0)


def solve(data_file: str = 'd_081.txt') -> str:
    '''Problem 81 - Path sum: two ways'''
    matrix = read_matrix(data_file)
    result = find_min_path(matrix)
    return str(result)


def test_simplified_version() -> None:
    answer = solve(data_file='d_081.basic.txt')
    assert type(answer) == str
    assert answer == '2427'


def test_answer() -> None:
    answer = solve()
    assert type(answer) == str
    assert answer == '427337'


if __name__ == '__main__':
    print(solve())
