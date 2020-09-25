# Largest palindrome product
# Problem 4
# A palindromic number reads the same both ways.
# The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

# Find the largest palindrome made from the product of two 3-digit numbers.

from typing import List, Tuple


def is_palindrome(n: int) -> bool:
    '''checks if n is a palindrome'''
    return str(n) == str(n)[::-1]


def add_to_product_queue(queue: List[Tuple[int, int, int]], factor_a: int, factor_b: int) -> None:
    '''inserts the product and both factors to the correct position within the queue'''
    product = factor_a * factor_b
    index = 0
    while index < len(queue) and product < queue[index][0]:
        index += 1
    if index >= len(queue) or not (queue[index][1] == factor_a and queue[index][2] == factor_b):
        queue.insert(index, (product, factor_a, factor_b))


def solve(digits: int = 3) -> str:
    '''Problem 4 - Largest palindrome product'''
    max_factor = 10 ** digits - 1
    product_queue = [(max_factor * max_factor, max_factor, max_factor)]
    while True:
        if is_palindrome(product_queue[0][0]):
            return str(product_queue[0][0])
        product, factor_a, factor_b = product_queue.pop(0)
        add_to_product_queue(product_queue, factor_a, factor_b - 1)
        if factor_a > factor_b:
            add_to_product_queue(product_queue, factor_a - 1, factor_b)


if __name__ == '__main__':
    print(solve())
