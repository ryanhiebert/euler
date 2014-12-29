#!/usr/bin/env python3

"""Project Euler Problem 03

The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
"""

from math import sqrt


def is_prime(i):
    """Determine if a number is a prime number.

    This is extremly inefficient, but it is very simple.
    """
    return all(i % mod != 0 for mod in range(2, int(sqrt(i))))


def solve():
    """Solve the problem."""
    number = 600851475143
    primes = filter(is_prime, range(2, int(sqrt(number)) + 1))

    remainder = number

    for prime in primes:
        while remainder % prime == 0:
            if prime == remainder:
                return prime
            else:
                remainder = remainder / prime


if __name__ == '__main__':
    print(__doc__)
    print(solve())
