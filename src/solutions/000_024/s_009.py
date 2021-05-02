# Special Pythagorean triplet
# Problem 9
# https://projecteuler.net/problem=9

# A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

# a2 + b2 = c2
# For example, 32 + 42 = 9 + 16 = 25 = 52.

# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.


def solve(triplet_sum: int = 1000) -> str:
    '''Problem 9 - Special Pythagorean triplet'''
    squares = set()
    for x in range(1, triplet_sum):
        squares.add(x ** 2)
    for c in range(triplet_sum // 3, triplet_sum):
        for b in range(c - 1, (c - 1) // 2, -1):
            a_squared = c ** 2 - b ** 2
            a = int(a_squared ** 0.5)
            if a_squared in squares and a + b + c == triplet_sum:
                # print(f'{a}^2 + {b}^2 = {c}^2, {a **2} + {b**2} = {c**2}')
                return str(a * b * c)
    return '0'


def test_simplified_version() -> None:
    answer = solve(triplet_sum=30)
    assert type(answer) == str
    assert answer == '780'


def test_answer() -> None:
    answer = solve()
    assert type(answer) == str
    assert answer == '31875000'


if __name__ == '__main__':
    print(solve())
