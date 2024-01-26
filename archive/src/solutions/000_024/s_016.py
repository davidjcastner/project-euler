# Power digit sum
# Problem 16
# https://projecteuler.net/problem=16

# 2**15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

# What is the sum of the digits of the number 2**1000?


def solve(base: int = 2, exponent: int = 1000) -> str:
    '''Problem 16 - Power digit sum'''
    product = base**exponent
    digits = (int(c) for c in str(product))
    return str(sum(digits))


def test_simplified_version() -> None:
    answer = solve(base=2, exponent=15)
    assert type(answer) == str
    assert answer == '26'


def test_answer() -> None:
    answer = solve()
    assert type(answer) == str
    assert answer == '1366'


if __name__ == '__main__':
    print(solve())
