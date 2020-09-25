# Maximum path sum II
# Problem 67
# By starting at the top of the triangle below and moving to adjacent numbers on the row below,
# the maximum total from top to bottom is 23.

# 3
# 7 4
# 2 4 6
# 8 5 9 3

# That is, 3 + 7 + 4 + 9 = 23.

# Find the maximum total from top to bottom in triangle.txt (right click and 'Save Link/Target As...'),
# a 15K text file containing a triangle with one-hundred rows.

# NOTE: This is a much more difficult version of Problem 18.
# It is not possible to try every route to solve this problem, as there are 299 altogether!
# If you could check one trillion (1012) routes every second it would take over twenty billion years to check them all.
# There is an efficient algorithm to solve it. ;o)

import os
import pathlib


def solve() -> int:
    '''Problem 67 - Maximum path sum II'''
    data_file_path = os.path.join(pathlib.Path(__file__).parent.absolute(), 'input_data', 'pe_067.txt')
    with open(data_file_path) as raw_data:
        triangle_string = raw_data.read()
    triangle_series = [[int(n) for n in line.split()] for line in triangle_string.split('\n')]
    for depth in range(len(triangle_series) - 2, -1, -1):
        for index in range(len(triangle_series[depth])):
            triangle_series[depth][index] = triangle_series[depth][index] + max(triangle_series[depth + 1][index], triangle_series[depth + 1][index + 1])
    return triangle_series[0][0]


if __name__ == '__main__':
    print(solve())
