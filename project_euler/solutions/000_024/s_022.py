# Names scores
# Problem 22
# Using names.txt (right click and 'Save Link/Target As...'),
# a 46K text file containing over five-thousand first names, begin by sorting it into alphabetical order.
# Then working out the alphabetical value for each name,
# multiply this value by its alphabetical position in the list to obtain a name score.

# For example, when the list is sorted into alphabetical order,
# COLIN, which is worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list.
# So, COLIN would obtain a score of 938 × 53 = 49714.

# What is the total of all the name scores in the file?

import re
from project_euler.data.util import read_data


def solve(data_file: str = 'd_022.txt') -> str:
    '''Problem 22 - Names scores'''
    data = read_data(data_file)
    names = re.split('[^A-Z]+', data)[1:-1]
    names.sort()
    scores = [(i + 1) * sum([ord(c) - 64 for c in name]) for i, name in enumerate(names)]
    return str(sum(scores))


if __name__ == '__main__':
    print(solve())
