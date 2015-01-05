#!/usr/bin/env python3

"""Project Euler Problem 20

n! means n × (n − 1) × ... × 3 × 2 × 1

For example, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800,
and the sum of the digits in the number 10! is
3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.

Find the sum of the digits in the number 100!
"""


def fact(num):
    if num == 1:
        return 1

    return num * fact(num - 1)


def solve():
    """Solve the problem."""
    return sum(map(int, str(fact(100))))


if __name__ == '__main__':
    print(__doc__)
    print(solve())
