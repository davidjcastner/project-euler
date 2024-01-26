# Lattice paths
# Problem 15
# https://projecteuler.net/problem=15

# Starting in the top left corner of a 2×2 grid,
# and only being able to move to the right and down,
# there are exactly 6 routes to the bottom right corner.

# How many such routes are there through a 20×20 grid?

from src.lib.calculate import factorial


def n_choose_k(n: int, k: int) -> int:
    '''returns n choose k'''
    return factorial(n) // (factorial(k) * factorial(n - k))


def solve(grid_width: int = 20, grid_height: int = 20) -> str:
    '''Problem 15 - Lattice paths'''
    return str(n_choose_k(grid_width + grid_height, grid_height))


def test_simplified_version() -> None:
    answer = solve(grid_width=2, grid_height=2)
    assert type(answer) == str
    assert answer == '6'


def test_answer() -> None:
    answer = solve()
    assert type(answer) == str
    assert answer == '137846528820'


if __name__ == '__main__':
    print(solve())
