# Longest Collatz sequence
# Problem 14
# The following iterative sequence is defined for the set of positive integers:

# n → n/2 (n is even)
# n → 3n + 1 (n is odd)

# Using the rule above and starting with 13, we generate the following sequence:

# 13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
# It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms.
# Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.

# Which starting number, under one million, produces the longest chain?

# NOTE: Once the chain starts the terms are allowed to go above one million.


def collatz_length(n: int) -> int:
    '''returns the length of the collatz sequence for c'''
    if not hasattr(collatz_length, 'look_up'):
        collatz_length.look_up = {1: 1}  # type: ignore
    if n in collatz_length.look_up:  # type: ignore
        return collatz_length.look_up[n]  # type: ignore
    else:
        next_value = n // 2 if n % 2 == 0 else 3 * n + 1
        length = collatz_length(next_value) + 1
        collatz_length.look_up[n] = length  # type: ignore
        return length


def solve() -> int:
    '''Problem 14 - Longest Collatz sequence'''
    max_length, value = 1, 1
    limit = 10 ** 6
    for n in range(1, limit):
        length = collatz_length(n)
        if length > max_length:
            max_length = length
            value = n
    return value


if __name__ == '__main__':
    print(solve())
