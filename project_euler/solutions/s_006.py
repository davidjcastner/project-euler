# Sum square difference
# Problem 6
# The sum of the squares of the first ten natural numbers is,

# The square of the sum of the first ten natural numbers is,

# Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is .

# Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.


def int_range_sum(start: int, end: int, divisor: int) -> int:
    '''returns the sum of all integers in the range [start, end] divisible by divisor'''
    calc_start = start // divisor
    calc_end = end // divisor
    return ((calc_start + calc_end) * (calc_end - calc_start + 1) // 2) * divisor


def sum_of_squares(n: int) -> int:
    '''returns the sum of squares'''
    return n * (n + 1) * (2 * n + 1) // 6


def solve() -> int:
    '''Problem 6 - Sum square difference'''
    n = 100
    return int_range_sum(1, n, 1) ** 2 - sum_of_squares(n)


if __name__ == "__main__":
    print(solve())
