# Lexicographic permutations
# Problem 24
# https://projecteuler.net/problem=24

# A permutation is an ordered arrangement of objects.
# For example, 3124 is one possible permutation of the digits
# 1, 2, 3 and 4. If all of the permutations are listed numerically
# or alphabetically, we call it lexicographic order. The
# lexicographic permutations of 0, 1 and 2 are:
# 012 021 102 120 201 210
# What is the millionth lexicographic permutation of the digits
# 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?

import functools


@functools.cache
def fact(n: int) -> int:
    return n * fact(n - 1) if n else 1


def solve(items: set[str] = set([str(x) for x in range(10)]), n: int = 1_000_000) -> str:
    '''Problem 24 - Lexicographic permutations'''
    # total permutations = len(items)!
    # reset n to start at 0
    n = n - 1
    assert n >= 0 and n < fact(len(items))
    sorted_items = list(items)
    sorted_items.sort()
    solution = ''
    k = len(items) - 1
    remain = n
    while len(sorted_items) > 0:
        fact_k = fact(k)
        index = remain // fact_k
        remain = remain - (index * fact_k)
        # pop item at index and add to solution
        solution = solution + sorted_items.pop(index)
        k = k - 1
    return solution


def test_simplified_version() -> None:
    answer = solve(items=set([str(x) for x in range(3)]), n=3)
    assert type(answer) == str
    assert answer == '102'
    answer = solve(items=set([str(x) for x in range(3)]), n=4)
    assert answer == '120'


def test_answer() -> None:
    answer = solve()
    assert type(answer) == str
    assert answer == '2783915460'


if __name__ == '__main__':
    print(solve())
