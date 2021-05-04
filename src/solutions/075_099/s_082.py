# Path sum: three ways
# Problem 82
# https://projecteuler.net/problem=82

# NOTE: This problem is a more challenging version of Problem 81.
# The minimal path sum in the 5 by 5 matrix below, by starting in any cell in
# the left column and finishing in any cell in the right column, and only moving
# up, down, and right, is indicated in red and bold; the sum is equal to 994.

# 131 & 673 & 234 & 103 &  18
# 201 &  96 & 342 & 965 & 150
# 630 & 803 & 746 & 422 & 111
# 537 & 699 & 497 & 121 & 956
# 805 & 732 & 524 &  37 & 331

# Find the minimal path sum from the left column to the right column in
# matrix.txt (right click and "Save Link/Target As..."), a 31K text file
# containing an 80 by 80 matrix.

from typing import Callable
from src.lib.struct.Matrix import Matrix
from src.lib.utility import read_matrix


def find_min_path(
        matrix: Matrix,
        start: tuple[int, int],
        is_end: Callable[[int, int], bool]) -> int:
    # start at one locations and add all
    pass


def solve(data_file: str = 'd_082.txt') -> str:
    '''Problem 82 - Path sum: three ways'''
    matrix = read_matrix(data_file)

    def is_end_location(row: int, col: int) -> bool:
        '''returns true if the location is on the right of the matrix'''
        return col == (matrix.cols - 1)
    # find minimum of all min paths for locations on the left
    answer = min(find_min_path(
        matrix=matrix,
        start=(row, 0),
        is_end=is_end_location) for row in range(matrix.rows))
    return str(answer)


def test_simplified_version() -> None:
    answer = solve(data_file='d_082.basic.txt')
    assert type(answer) == str
    assert answer == '994'


def test_answer() -> None:
    answer = solve()
    assert type(answer) == str
    assert answer == '0'


if __name__ == '__main__':
    # print(solve())
    print(solve(data_file='d_082.basic.txt'))
