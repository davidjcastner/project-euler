# Sum square difference
# Problem 6
# The sum of the squares of the first ten natural numbers is,

# The square of the sum of the first ten natural numbers is,

# Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is .

# Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

from valkyrie_util.calculate import range_sum_int, sum_of_squares


def solve(n: int = 100) -> str:
    '''Problem 6 - Sum square difference'''
    return str(range_sum_int(1, n) ** 2 - sum_of_squares(n))


if __name__ == '__main__':
    print(solve())
