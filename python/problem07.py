#!/usr/bin/env python3

"""Project Euler Problem 07

By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can
see that the 6th prime is 13.

What is the 10 001st prime number?
"""


def solve():
    """Solve the problem."""
    cache = []
    i = 2

    while len(cache) < 10001:
        if not any(i % prime == 0 for prime in cache):
            cache.append(i)
        i += 1

    return cache[-1]


if __name__ == '__main__':
    print(__doc__)
    print(solve())
