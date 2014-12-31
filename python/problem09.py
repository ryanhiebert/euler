#!/usr/bin/env python3

"""Project Euler Problem 09

A Pythagorean triplet is a set of three natural numbers,
a < b < c, for which,

a ** 2 + b ** 2 = c ** 2
For example, 3 ** 2 + 4 ** 2 = 9 + 16 = 25 = 5 ** 2.

There exists exactly one Pythagorean triplet for which
a + b + c = 1000. Find the product abc.
"""


def solve():
    """Solve the problem."""
    for a in range(1, 999):
        for b in range(1, 999):
            c = 1000 - a - b

            if c > 1 and a < b < c and a ** 2 + b ** 2 == c ** 2:
                return a * b * c


if __name__ == '__main__':
    print(__doc__)
    print(solve())
