#!/usr/bin/env python3

"""Project Euler Problem 06

The sum of the squares of the first ten natural numbers is,

    1 ** 2 + 2 ** 2 + ... + 10 ** 2 = 385

The square of the sum of the first ten natural numbers is,

    (1 + 2 + ... + 10) ** 2 = 55 ** 2 = 3025

Hence the difference between the sum of the squares of the first ten
natural numbers and the square of the sum is 3025 − 385 = 2640.

Find the difference between the sum of the squares of the first one
hundred natural numbers and the square of the sum.
"""


square = lambda x: x ** 2


def solve():
    """Solve the problem."""
    numbers = range(1, 101)  # 1 - 100
    sum_of_squares = sum(map(square, numbers))
    square_of_sum = square(sum(numbers))
    return square_of_sum - sum_of_squares


if __name__ == '__main__':
    print(__doc__)
    print(solve())
