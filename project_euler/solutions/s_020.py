# Factorial digit sum
# Problem 20
# n! means n × (n − 1) × ... × 3 × 2 × 1

# For example, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800,
# and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.

# Find the sum of the digits in the number 100!

from typing import List


def multiply_digits(digit_list: List[int], multiplier: int, base: int = 10) -> List[int]:
    '''multiplies a list of digits by a small number,
    each digit in the list should represent the value digit_list[index] * base ** index'''
    product, magnitude, remainder = [], 0, 0
    while remainder > 0 or magnitude < len(digit_list):
        if magnitude < len(digit_list):
            remainder += digit_list[magnitude] * multiplier
        product.append(remainder % base)
        remainder = remainder // base
        magnitude += 1
    return product


def factorial_digits(n: int) -> List[int]:
    '''returns n! as a list of digits'''
    if n == 0 or n == 1:
        return [1]
    else:
        return multiply_digits(factorial_digits(n - 1), n)


def solve() -> int:
    '''Problem 20 - Factorial digit sum'''
    n = 100
    return sum(factorial_digits(n))


if __name__ == '__main__':
    print(solve())
