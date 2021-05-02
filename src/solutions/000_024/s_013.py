# Large sum
# Problem 13
# Work out the first ten digits of the sum of the following one-hundred 50-digit numbers.

from project_euler.data.util import read_data
from project_euler.lib.large import large_number_sum, large_number_to_string, string_to_large_number


def solve(digits: int = 10, data_file: str = 'd_013.txt') -> str:
    '''Problem 13 - Large sum'''
    data = read_data(data_file)
    addends = [string_to_large_number(line) for line in data.splitlines()]
    return large_number_to_string(large_number_sum(*addends))[:digits]


if __name__ == '__main__':
    print(solve())
