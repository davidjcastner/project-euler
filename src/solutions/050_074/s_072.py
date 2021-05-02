# Counting fractions
# Problem 72
# https://projecteuler.net/problem=72

# Consider the fraction, n/d, where n and d are positive integers. If n<d and
# HCF(n,d)=1, it is called a reduced proper fraction.
# If we list the set of reduced proper fractions for d <= 8 in ascending order
# of size, we get:
# 1/8, 1/7, 1/6, 1/5, 1/4, 2/7, 1/3, 3/8, 2/5, 3/7, 1/2, 4/7, 3/5, 5/8, 2/3,
# 5/7, 3/4, 4/5, 5/6, 6/7, 7/8
# It can be seen that there are 21 elements in this set.
# How many elements would be contained in the set of reduced proper fractions
# for d <= 1,000,000?


def solve(d: int = 1_000_000) -> str:
    '''Problem 72 - Counting fractions'''
    # for x in range(1,d+1), if x is prime then x - 1 fractions are added
    # if x is composite, then x - highest multiple is added?
    # 1: []
    # 2: [1/2] 2
    # 3: [1/3, 2/3] 3
    # 4: [1/4, 3/4] 2*2
    # 5: [1/5, 2/5, 3/5, 4/5] 5
    # 6: [1/6, 5/6] 2*3
    # 7: [1/7, 2/7, 3/7, 4/7, 5/7, 6/7] 7
    # 8: [1/8, 3/8, 5/8, 7/8] 2*2*2
    # 9: [1/9, 2/9, 4/9, 5/9, 7/9, 8/9] 3*3
    # 10: [1/10, 3/10, 7/10, 9/10] 2*5
    # 11: [...] 11
    # 12: [1/12, 5/12, 7/12, 11/12] 2*2*3
    # 13: [...] 13
    # 14: [1/14, 3/14, 5/14, 9/14, 11/14, 13/14] 2*7
    # 15: [1/15, 2/15, 4/15, 7/15, 8/15, 11/15, 13/15, 14/15] 3*5

    # look at value for value when dividing by each unique prime divisor
    # 2: 2, 1
    # 3: 3, 2
    # 4: 2*2, 2 (3-1)
    # 5: 5, 4
    # 6: 2*3, 2 (5-2-1)
    # 7: 7, 6
    # 8: 2*2*2, 4 (7-3)
    # 9: 3*3, 6 (8-2)
    # 10: 2*5, 4 (9-4-1)
    # 11: 11, 10
    # 12: 2*2*3, (11-3-2)
    # 13: 13, 12
    # 14: 2*7, 6 (13-6-1)
    # 30: 2*3*5, (29-4-2-1)
    # ???
    return str()


if __name__ == '__main__':
    print(solve())
