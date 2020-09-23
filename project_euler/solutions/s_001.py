# Multiples of 3 and 5
# Problem 1

# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

# Find the sum of all the multiples of 3 or 5 below 1000.


def int_range_sum(start: int, end: int, divisor: int) -> int:
    '''returns the sum of all integers in the range [start, end] divisible by divisor'''
    calc_start = start // divisor
    calc_end = end // divisor
    return ((calc_start + calc_end) * (calc_end - calc_start + 1) // 2) * divisor


def solve() -> int:
    '''Problem 1 - Multiples of 3 and 5'''
    # can be done with math:
    # sum of multiples of 3 in the range [1, 1000)
    # + sum of multiples of 5 in the range [1, 1000)
    # - sum of multiples of 15 in the range [1, 1000)
    start, end = 0, 999
    return int_range_sum(start, end, 3) + int_range_sum(start, end, 5) - int_range_sum(start, end, 15)


if __name__ == "__main__":
    print(solve())
