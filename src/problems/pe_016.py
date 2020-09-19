# Power digit sum
# Problem 16
# 215 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

# What is the sum of the digits of the number 21000?

from typing import List


def multiple_digits(digit_list: List[int], multiplier: int, base: int = 10) -> List[int]:
    '''multiples a list of digits by a small number, each digit in the list shoudl represent the value digit_list[index] * base ** index'''
    product, magnitude, remainder = [], 0, 0
    while remainder > 0 or magnitude < len(digit_list):
        if magnitude < len(digit_list):
            remainder += digit_list[magnitude] * multiplier
        product.append(remainder % base)
        remainder = remainder // base
        magnitude += 1
    return product


def solve() -> int:
    '''Problem 16 - Power digit sum'''
    base, exponent = 2, 1000
    product = [1]
    for x in range(exponent):
        product = multiple_digits(product, base)
    return sum(product)


if __name__ == "__main__":
    print(solve())
