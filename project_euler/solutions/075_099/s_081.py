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

from project_euler.lib.struct.Matrix import Matrix
from project_euler.data.util import read_data


def get_matrix_from_data(data_file: str) -> Matrix:
    # data is csv strings
    data = read_data(data_file)
    data = data.splitlines()
    data = [row.split(',') for row in data]
    data = [[int(val) for val in row] for row in data]
    return Matrix.from_data(data)


def find_min_path(m: Matrix) -> int:
    '''finds the min path in the matrix from top left to bottom right,
    only uses down and right directions for pathing'''
    min_values = m.blank_copy()
    for row, col in m.each_row_col(reverse=True):
        node_value = m.get(row=row, col=col)
        min_path = 0
        if row + 1 == m.rows and col + 1 == m.cols:
            min_path = node_value
        elif row + 1 == m.rows:
            min_path = node_value + min_values.get(row=row, col=col + 1)
        elif col + 1 == m.cols:
            min_path = node_value + min_values.get(row=row + 1, col=col)
        else:
            min_path = node_value + min(
                min_values.get(row=row, col=col + 1),
                min_values.get(row=row + 1, col=col))
        min_values.set(row=row, col=col, value=min_path)
    return min_values.get(row=0, col=0)


def solve(data_file: str = 'd_081.txt') -> str:
    '''Problem 81 - Path sum: two ways'''
    matrix = get_matrix_from_data(data_file)
    result = find_min_path(matrix)
    return str(result)


if __name__ == '__main__':
    print(solve())
