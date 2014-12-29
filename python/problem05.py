#!/usr/bin/env python3

"""Project Euler Problem 05

2520 is the smallest number that can be divided by each of the numbers
from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of
the numbers from 1 to 20?
"""

from itertools import chain

# Primes less than 20
primes = [1, 2, 3, 5, 7, 11, 13, 17, 19]

def factorize(i):
    """Find the prime factors of this number."""
    if i in primes:
        return (i,)
    else:
        for prime in primes[1:]:
            if i % prime == 0:
                return tuple(chain((prime,), factorize(i//prime)))


def dict_factorize(i):
    """Make a dictionary of prime factors to quantities."""
    factors = {}
    for factor in factorize(i):
        if factor not in factors:
            factors[factor] = 0
        factors[factor] += 1
    return factors


def solve():
    """Solve the problem."""
    integers = range(1, 21)  # 1 - 20
    factorizements = map(dict_factorize, integers)

    factors = {prime: 0 for prime in primes}
    for factorizement in factorizements:
        for factor, quantity in factorizement.items():
            if quantity > factors[factor]:
                factors[factor] = quantity

    answer = 1
    for factor, quantity in factors.items():
        answer *= factor ** quantity

    return answer


if __name__ == '__main__':
    print(__doc__)
    print(solve())
