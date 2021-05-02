# Longest Collatz sequence
# Problem 14
# https://projecteuler.net/problem=14

# The following iterative sequence is defined for the set of positive integers:

# n → n/2 (n is even)
# n → 3n + 1 (n is odd)

# Using the rule above and starting with 13, we generate the following sequence:

# 13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
# It can be seen that this sequence (starting at 13 and finishing at 1) contains
# 10 terms.
# Although it has not been proved yet (Collatz Problem), it is thought that all
# starting numbers finish at 1.

# Which starting number, under one million, produces the longest chain?

# NOTE: Once the chain starts the terms are allowed to go above one million.

from project_euler.lib.collatz import collatz_length


def solve(limit: int = 10 ** 6) -> str:
    '''Problem 14 - Longest Collatz sequence'''
    max_length, value = 1, 1
    for n in range(1, limit):
        length = collatz_length(n)
        if length > max_length:
            max_length, value = length, n
    return str(value)


def test_simplified_version() -> None:
    answer = solve(limit=10)
    assert type(answer) == str
    assert answer == '9'


def test_answer() -> None:
    answer = solve()
    assert type(answer) == str
    assert answer == '837799'


if __name__ == '__main__':
    print(solve())
