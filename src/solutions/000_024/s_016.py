# Power digit sum
# Problem 16
# 2**15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

# What is the sum of the digits of the number 2**1000?

from project_euler.lib.large import large_number_multiply


def solve(base: int = 2, exponent: int = 1000) -> str:
    '''Problem 16 - Power digit sum'''
    product = [1]
    for x in range(exponent):
        product = large_number_multiply(product, base)
    return str(sum(product))


if __name__ == '__main__':
    print(solve())
