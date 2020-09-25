# Factorial digit sum
# Problem 20
# n! means n × (n − 1) × ... × 3 × 2 × 1

# For example, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800,
# and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.

# Find the sum of the digits in the number 100!

from valkyrie_util.large import large_number_multiply


def solve(n: int = 100) -> int:
    '''Problem 20 - Factorial digit sum'''
    product = [1]
    for multiplier in range(2, n):
        product = large_number_multiply(product, multiplier)
    return str(sum(product))


if __name__ == '__main__':
    print(solve())
