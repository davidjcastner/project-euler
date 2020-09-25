# Lattice paths
# Problem 15
# Starting in the top left corner of a 2×2 grid,
# and only being able to move to the right and down,
# there are exactly 6 routes to the bottom right corner.


# How many such routes are there through a 20×20 grid?

def factorial(n: int) -> int:
    '''returns n!'''
    if n == 1 or n == 0:
        return 1
    else:
        return n * factorial(n - 1)


def n_choose_k(n: int, k: int) -> int:
    '''returns n choose k'''
    return factorial(n) // (factorial(k) * factorial(n - k))


def solve() -> int:
    '''Problem 15 - Lattice paths'''
    grid_size = 20
    return n_choose_k(2 * grid_size, grid_size)


if __name__ == '__main__':
    print(solve())
