# Even Fibonacci Numbers
# Problem 2
# https://projecteuler.net/problem=2

# Each new term in the Fibonacci sequence is generated by adding the previous
# two terms. By starting with 1 and 2, the first 10 terms will be: 1, 2, 3, 5,
# 8, 13, 21, 34, 55, 89, ... By considering the terms in the Fibonacci sequence
# whose values do not exceed four million, find the sum of the even-valued
# terms.


def fibonacci_generator(a: int = 1, b: int = 1):
    """iterates through the fibonacci sequence using starting values"""
    assert isinstance(a, int) and isinstance(b, int)
    while True:
        yield a
        a, b = b, a + b


def solve() -> str:
    """Problem 2 - Even Fibonacci Numbers"""
    fib = fibonacci_generator()
    total = 0
    while (n := next(fib)) < 4_000_000:
        if n % 2 == 0:
            total += n
    return str(total)


if __name__ == '__main__':
    print(solve())
