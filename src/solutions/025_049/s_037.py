# Truncatable primes
# Problem 37
# https://projecteuler.net/problem=37

# The number 3797 has an interesting property. Being prime itself, it is
# possible to continuously remove digits from left to right, and remain prime
# at each stage: 3797, 797, 97, and 7. Similarly we can work from right to left:
# 3797, 379, 37, and 3.
# Find the sum of the only eleven primes that are both truncatable from left to
# right and right to left.
# NOTE: 2, 3, 5, and 7 are not considered to be truncatable primes.


from src.lib.primes import is_prime


def append_digit(number: int, digit: int) -> int:
    '''adds the digit to the right'''
    return number * 10 + digit


def is_trunc_left_to_right(number: int) -> bool:
    '''checks if a number is truncatable left to right while remaining prime'''
    while number > 0:
        if not is_prime(number):
            return False
        number = int(str(number)[1:]) if number >= 10 else 0
    return True


def is_trunc_right_to_left(number: int) -> bool:
    '''checks if a number is truncatable right to left while remaining prime'''
    while number > 0:
        if not is_prime(number):
            return False
        number = number // 10
    return True


def is_truncatable_prime(number: int) -> bool:
    if number < 10:
        return False
    return is_trunc_right_to_left(number) and is_trunc_left_to_right(number)


def initialize_stack() -> list[int]:
    '''returns a list of 2 digit truncatable primes'''
    return [n for n in range(10, 100) if is_truncatable_prime(n)]


def solve() -> str:
    '''Problem 37 - Truncatable primes'''
    # start with 2, 3, 5, 7
    # rightmost digit must be 2, 3, 5, 7
    # primes with two or more digits in base ten, must end in 1, 3, 7, 9
    # so when removing right to left each digit except leftmost must be one
    # of those

    known = set()
    stack = [2, 3, 5, 7]
    while len(stack) > 0:
        number = stack.pop()
        if is_truncatable_prime(number):
            known.add(number)
        if is_prime(number):
            for digit in {1, 3, 7, 9}:
                stack.append(append_digit(number, digit))
    return str(sum(known))


# no trivial case for testing
# def test_simplified_version() -> None:
#     answer = solve()
#     assert type(answer) == str
#     assert answer == '0'


def test_answer() -> None:
    answer = solve()
    assert type(answer) == str
    assert answer == '748317'


if __name__ == '__main__':
    print(solve())
