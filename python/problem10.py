#!/usr/bin/env python3

"""Project Euler Problem 10

The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
"""

def primes(limit):
    """Find and iterate over the primes in order."""
    cache = []
    i = 2

    while i < limit:
        if not any(i % prime == 0 for prime in cache):
            cache.append(i)
        i += 1

    return cache


def solve():
    """Solve the problem."""
    return sum(primes(limit=2000000))


if __name__ == '__main__':
    print(__doc__)
    print(solve())
