'''operations for dates'''
from __future__ import annotations


class Date:
    '''
    tracker for days

    dayofweek:
    0 - Monday
    1 - Tuesday
    ...
    6 - Sunday
    '''

    def __init__(self, day: int, month: int, year: int, dayofweek: int = 0) -> None:
        self.day = day
        self.month = month
        self.year = year
        self.dayofweek = dayofweek

    def __str__(self) -> str:
        return f'{self.year}-{str(self.month).zfill(2)}-{str(self.day).zfill(2)} [{self.dayofweek}]'

    def copy(self) -> Date:
        return Date(self.day, self.month, self.year, self.dayofweek)

    # def __eq__(self, other: Date) -> bool:
    #     return self.year == other.year and self.month == other.month and self.day == other.day

    # def __gt__(self, other: Date) -> bool:
    #     return not (self.year < other.year or self.month < other.month or self.day <= other.day)

    # def __gte__(self, other: Date) -> bool:
    #     return not (self.year < other.year or self.month < other.month or self.day < other.day)

    # def __lt__(self, other: Date) -> bool:
    #     return not (self.year > other.year or self.month > other.month or self.day >= other.day)

    # def __lte__(self, other: Date) -> bool:
    #     return not (self.year > other.year or self.month > other.month or self.day > other.day)


def __is_leap_year(d: Date) -> bool:
    return (d.year % 400 == 0) or (d.year % 100 != 0 and d.year % 4 == 0)


def __days_in_month(d: Date) -> int:
    # February is special case
    if d.month == 2:
        return 29 if __is_leap_year(d) else 28
    # April 4, June 6, September 9, November 11
    # have thirty days
    if d.month in {4, 6, 9, 11}:
        return 30
    # all the rest have 31 days
    return 31


def increment_day(d: Date) -> Date:
    n = d.copy()
    n.day = n.day + 1
    n.dayofweek = (n.dayofweek + 1) % 7
    # check for month overflow
    if n.day > __days_in_month(d):
        n.day = 1
        n.month = n.month + 1
        # check for year overflow
        if n.month > 12:
            n.month = 1
            n.year = n.year + 1
    return n


def increment_month(d: Date) -> Date:
    '''if day is 31 then go to 30 for next month'''
    n = d.copy()
    days = n.day
    n.month = n.month + 1
    # check for year overflow
    if n.month > 12:
        n.month = 1
        n.year = n.year + 1
    nd = __days_in_month(n)
    if n.day > nd:
        n.day = nd
        days = days - (n.day - nd)
    n.dayofweek = (n.dayofweek + days) % 7
    return n
