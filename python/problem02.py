#!/usr/bin/env python3

"""Project Euler Problem 02

Each new term in the Fibonacci sequence is generated by adding the
previous two terms. By starting with 1 and 2, the first 10 terms will
be:

1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

By considering the terms in the Fibonacci sequence whose values do not
exceed four million, find the sum of the even-valued terms.
"""


def fib(stop):
    """Generate the fibonacci numbers preceding stop."""
    i, j = 0, 1
    while i < stop:
        k = i + j
        yield k
        i, j = j, k


def even(i):
    """Determine if an integer is even."""
    return i % 2 == 0


def solve():
    """Solve the problem."""
    # Stop must be 1 more than the limit: the limit is not inclusive
    return sum(filter(even, fib(4000001)))


if __name__ == '__main__':
    print(__doc__)
    print(solve())