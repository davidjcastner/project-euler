# Large sum
# Problem 13
# Work out the first ten digits of the sum of the following one-hundred 50-digit numbers.


def solve() -> str:
    '''Problem 13 - Large sum'''
    digits = 50
    number_string = ''
    # convert each number to a list where each value in the list represents value * 10 ** index
    numbers = [[int(c) for c in num[::-1]] for num in number_string.split()]
    total, magnitude, remainder = [], 0, 0
    while remainder > 0 or magnitude < digits:
        if magnitude < digits:
            for num in numbers:
                remainder += num[magnitude]
        total.append(remainder % 10)
        remainder = remainder // 10
        magnitude += 1
    return str().join([str(n) for n in total[-1:-11:-1]])


if __name__ == "__main__":
    print(solve())
