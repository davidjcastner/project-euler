# Number spiral diagonals
# Problem 28
# https://projecteuler.net/problem=28

# Starting with the number 1 and moving to the right in a
# clockwise direction a 5 by 5 spiral is formed as follows:
# 21 22 23 24 25
# 20  7  8  9 10
# 19  6  1  2 11
# 18  5  4  3 12
# 17 16 15 14 13
# It can be verified that the sum of the numbers on the diagonals is 101.
# What is the sum of the numbers on the diagonals in a 1001 by 1001
# spiral formed in the same way?


def solve(n: int = 1001) -> str:
    '''Problem 28 - Number spiral diagonals'''
    # difference between corners on an edge (25, 21, 17, 13) is 4 or n - 1
    # so total of all corners on each concentic square is
    # n**2 + n**2 - (n - 1) + n**2 - 2(n - 1) + n**2 - 3(n - 1)
    # or 4n**2 - 6n + 6
    # exception is 1 since no corners
    # sum of 4n**2 - 6n + 6 for range(3,n+1,2) + 1
    # could use gauss sum if n is way bigger
    assert n % 2 == 1 and n > 0
    answer = sum([4 * x**2 - 6 * x + 6 for x in range(3, n + 1, 2)]) + 1
    return str(answer)


def test_simplified_version() -> None:
    answer = solve(n=5)
    assert type(answer) == str
    assert answer == '101'


def test_answer() -> None:
    answer = solve()
    assert type(answer) == str
    assert answer == '669171001'


if __name__ == '__main__':
    print(solve())
