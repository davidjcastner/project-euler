# Double-base palindromes
# Problem 36
# https://projecteuler.net/problem=36

# The decimal number, 585 = 1001001001 (binary), is palindromic in both bases.
# Find the sum of all numbers, less than one million, which are palindromic in
# base 10 and base 2.
# (Please note that the palindromic number, in either base, may not include
# leading zeros.)

def is_palindrome(pal: list[int]) -> bool:
    '''checks if the items in the list make a palindrom,
    ie the first element equals last element'''
    size = len(pal)
    return all(pal[i] == pal[size - 1 - i] for i in range(size // 2))


def digits_by_base(n: int, base: int) -> list[int]:
    '''returns the digits of a number as a list'''
    assert isinstance(n, int) and n >= 0
    assert isinstance(base, int) and base >= 2
    digits = []
    remainder = n
    while remainder > 0:
        digits.append(remainder % base)
        remainder = remainder // base
    return digits[::-1]


def is_special(n: int) -> bool:
    '''checks if n in base 2 and 10 are palindromes'''
    return is_palindrome(
        digits_by_base(n, 10)) and is_palindrome(digits_by_base(n, 2))


def solve(limit: int = 1_000_000) -> str:
    '''Problem 36 - Double-base palindromes'''
    return str(sum(n for n in range(1, limit) if is_special(n)))


def test_simplified_version() -> None:
    answer = solve(limit=34)
    assert type(answer) == str
    assert answer == '58'


def test_answer() -> None:
    answer = solve()
    assert type(answer) == str
    assert answer == '872187'


if __name__ == '__main__':
    print(solve())
