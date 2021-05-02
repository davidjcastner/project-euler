# 1000-digit Fibonacci number
# Problem 25
# https://projecteuler.net/problem=25

# The Fibonacci sequence is defined by the recurrence relation:

# Fn = Fn−1 + Fn−2, where F1 = 1 and F2 = 1.
# Hence the first 12 terms will be:

# F1 = 1
# F2 = 1
# F3 = 2
# F4 = 3
# F5 = 5
# F6 = 8
# F7 = 13
# F8 = 21
# F9 = 34
# F10 = 55
# F11 = 89
# F12 = 144
# The 12th term, F12, is the first term to contain three digits.

# What is the index of the first term in the Fibonacci sequence to contain 1000
# digits?


from typing import Generator, List
from project_euler.lib.large import large_number_sum


def large_fibonacci() -> Generator[List[int], None, None]:
    '''iterates through the fibonaccie sequence using starting values'''
    a, b = [1], [1]
    while True:
        yield a
        a, b = b.copy(), large_number_sum(a, b)


def solve(digits: int = 1000) -> str:
    '''Problem 25 - 1000-digit Fibonacci number'''
    gen, index = large_fibonacci(), 0
    while True:
        large_n, index = next(gen), index + 1
        if len(large_n) >= digits:
            break
    return str(index)


def test_simplified_version() -> None:
    answer = solve(digits=3)
    assert type(answer) == str
    assert answer == '12'


def test_answer() -> None:
    answer = solve()
    assert type(answer) == str
    assert answer == '4782'


if __name__ == '__main__':
    print(solve())
