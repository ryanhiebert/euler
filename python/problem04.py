#!/usr/bin/env python3

"""Project Euler Problem 04

A palindromic number reads the same both ways. The largest palindrome
made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit
numbers.
"""

from operator import mul
from itertools import combinations


def is_palindrome(i):
    """Determine if the given integer is a palindrome."""
    return list(str(i)) == list(reversed(str(i)))


def multiply(nums):
    """Multiply the numbers."""
    return mul(*nums)

def solve():
    """Solve the problem."""
    three_digits = range(100, 1000)
    products = map(multiply, combinations(three_digits, 2))
    palindromes = filter(is_palindrome, products)
    return max(palindromes)


if __name__ == '__main__':
    print(__doc__)
    print(solve())
