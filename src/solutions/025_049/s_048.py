# Self powers
# Problem 48
# https://projecteuler.net/problem=48

# The series, 1**1 + 2**2 + 3**3 + ... + 10**10 = 10405071317.
# Find the last ten digits of the series, 1**1 + 2**2 + 3**3 + ... + 1000**1000.

def pow_last_digits(n: int, d: int) -> int:
    '''returns the last d digits of n**n'''
    pows = 1
    result = n
    while pows < n:
        result = (result * n) % pow(10, d)
        pows += 1
    return result


def add_last_digits(iterator: list[int], d: int) -> int:
    '''adds all integers in the iterator and returns the last d digits'''
    return sum(iterator) % pow(10, d)


def solve(n: int = 1000, d: int = 10) -> str:
    '''Problem 48 - Self powers'''
    answer = add_last_digits((pow_last_digits(x, d) for x in range(1, n + 1)), d)
    return str(answer)


if __name__ == '__main__':
    print(solve())
