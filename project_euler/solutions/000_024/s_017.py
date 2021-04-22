# Number letter counts
# Problem 17
# If the numbers 1 to 5 are written out in words: one, two, three, four, five,
# then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

# If all the numbers from 1 to 1000 (one thousand) inclusive were written out
# in words, how many letters would be used?


# NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and
# forty-two) contains 23 letters and 115 (one hundred and fifteen) contains
# 20 letters. The use of "and" when writing out numbers is in compliance with
# British usage.


from num2words import num2words


def strip_non_alpha(s: str) -> str:
    '''removes all non alpha characters'''
    result = ''
    for i in range(len(s)):
        if s[i].isalpha():
            result += s[i]
    return result


def solve(n: int = 1000) -> str:
    '''Problem 17 - Number letter counts'''
    s = 0
    for x in range(1, n + 1):
        s += len(strip_non_alpha(num2words(x)))
    return str(s)


if __name__ == '__main__':
    print(solve())
