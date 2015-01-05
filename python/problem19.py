#!/usr/bin/env python3

"""Project Euler Problem 19

You are given the following information, but you may prefer to do some
research for yourself.

* 1 Jan 1900 was a Monday.
* Thirty days has September,
  April, June and November.
  All the rest have thirty-one,
  Saving February alone,
  Which has twenty-eight, rain or shine.
  And on leap years, twenty-nine.
* A leap year occurs on any year evenly divisible by 4, but not on a
  century unless it is divisible by 400.

How many Sundays fell on the first of the month during the twentieth
century (1 Jan 1901 to 31 Dec 2000)?
"""

from datetime import date, timedelta


def sundays():
    """Iterate over the firsts of the month."""
    start = date(1901, 1, 1)
    sunday = start + timedelta(days=6 - start.weekday())

    delta = timedelta(weeks=1)
    while sunday <= date(2000, 12, 31):
        yield sunday
        sunday += delta


def solve():
    """Solve the problem."""
    return len([x for x in sundays() if x.day == 1])


if __name__ == '__main__':
    print(__doc__)
    print(solve())
