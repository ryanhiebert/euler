#!/usr/bin/env python3

"""Project Euler Problem 01

If we list all the natural numbers below 10 that are multiples of 3 or
5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.
"""


def mod(stop, mods):
    """Find all integers less than stop that are divisible by any modulos."""
    return (i for i in range(stop) if any(i % mod == 0 for mod in mods))

def solve():
    """Solve the problem."""
    return sum(mod(1000, (3, 5)))


if __name__ == '__main__':
    print(__doc__)
    print(solve())
