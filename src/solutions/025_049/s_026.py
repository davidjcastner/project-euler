# Reciprocal cycles
# Problem 26
# https://projecteuler.net/problem=26

# A unit fraction contains 1 in the numerator. The decimal representation of
# the unit fractions with denominators 2 to 10 are given:

# 1/2=0.5
# 1/3=0.(3)
# 1/4=0.25
# 1/5=0.2
# 1/6=0.1(6)
# 1/7=0.(142857)
# 1/8=0.125
# 1/9=0.(1)
# 1/10=0.1

# Where 0.1(6) means 0.166666..., and has a 1-digit recurring cycle. It can be
# seen that 1/7 has a 6-digit recurring cycle.
# Find the value of d < 1000 for which 1/d contains the longest recurring cycle
# in its decimal fraction part.


def cycle_length(n: int, base: int = 10) -> int:
    '''returns length of the recurring fractional part of 1/n'''
    assert isinstance(n, int) and n > 0
    assert isinstance(base, int) and base > 1
    remainder = 1 * base
    known = {remainder: 0}
    fractional = []
    is_repeating = False
    while remainder != 0:
        # calculate quotient and new remainder
        quotient = remainder // n
        remainder = remainder % n

        # move to next digit
        remainder = remainder * base
        fractional.append(quotient)

        # check for recurring remainders
        if remainder in known:
            is_repeating = True
            break
        else:
            known[remainder] = len(fractional)
    return len(fractional) - known[remainder] if is_repeating else 0


def solve(d: int = 1000) -> str:
    '''Problem 26 - Reciprocal cycles'''
    min_num = 0
    min_length = 0
    for n in range(1, d):
        length = cycle_length(n)
        if length > min_length:
            min_num = n
            min_length = length
    return str(min_num)


def test_simplified_version() -> None:
    answer = solve(d=10)
    assert type(answer) == str
    assert answer == '7'


def test_answer() -> None:
    answer = solve()
    assert type(answer) == str
    assert answer == '983'


if __name__ == '__main__':
    print(solve())
