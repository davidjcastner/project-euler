# Maximum path sum I
# Problem 18
# https://projecteuler.net/problem=18

# By starting at the top of the triangle below and moving to adjacent numbers
# on the row below, the maximum total from top to bottom is 23.

# 3
# 7 4
# 2 4 6
# 8 5 9 3

# That is, 3 + 7 + 4 + 9 = 23.

# Find the maximum total from top to bottom of the triangle below:

# 75
# 95 64
# 17 47 82
# 18 35 87 10
# 20 04 82 47 65
# 19 01 23 75 03 34
# 88 02 77 73 07 63 67
# 99 65 04 28 06 16 70 92
# 41 41 26 56 83 40 80 70 33
# 41 48 72 33 47 32 37 16 94 29
# 53 71 44 65 25 43 91 52 97 51 14
# 70 11 33 28 77 73 17 78 39 68 17 57
# 91 71 52 38 17 14 91 43 58 50 27 29 48
# 63 66 04 68 89 53 67 30 73 16 69 87 40 31
# 04 62 98 27 23 09 70 98 73 93 38 53 60 04 23

# NOTE: As there are only 16384 routes, it is possible to solve this problem by
# trying every route.
# However, Problem 67, is the same challenge with a triangle containing one -
# hundred rows;
# it cannot be solved by brute force, and requires a clever method!; o)


from project_euler.data.util import read_data


def solve(data_file: str = 'd_018.txt') -> str:
    '''Problem 18 - Maximum path sum I'''
    data = read_data(data_file)
    triangle_series = [[int(n) for n in line.split()] for line in data.splitlines()]
    for depth in range(len(triangle_series) - 2, -1, -1):
        for index in range(len(triangle_series[depth])):
            left_child_value = triangle_series[depth + 1][index]
            right_child_value = triangle_series[depth + 1][index + 1]
            triangle_series[depth][index] += max(left_child_value, right_child_value)
    return str(triangle_series[0][0])


def test_simplified_version() -> None:
    answer = solve(data_file='d_018.basic.txt')
    assert type(answer) == str
    assert answer == '23'


def test_answer() -> None:
    answer = solve()
    assert type(answer) == str
    assert answer == '1074'


if __name__ == '__main__':
    print(solve())
