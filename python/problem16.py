#!/usr/bin/env python3

"""Project Euler Problem 16

2 ** 15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

What is the sum of the digits of the number 2 ** 1000?
"""


def solve():
    """Solve the problem."""
    return sum(map(int, str(2 ** 1000)))


if __name__ == '__main__':
    print(__doc__)
    print(solve())
