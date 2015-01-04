#!/usr/bin/env python3

"""Project Euler Problem 15

Starting in the top left corner of a 2×2 grid, and only being able to
move to the right and down, there are exactly 6 routes to the bottom
right corner.

How many such routes are there through a 20×20 grid?
"""


def cache(fn):
    """Cache the return value of a function based on it's args."""
    fn.cache = {}
    def wrapper(*args):
        if args not in fn.cache:
            fn.cache[args] = fn(*args)
        return fn.cache[args]
    return wrapper


@cache
def moves(row, col):
    """Find out how many moves are possible to get from (0, 0) to the goal."""
    if row == 0 or col == 0:
        return 1

    row_moves = moves((row - 1), col) if row != 0 else 0
    col_moves = moves(row, (col - 1)) if col != 0 else 0

    return row_moves + col_moves


def solve():
    """Solve the problem."""
    return moves(20, 20)


if __name__ == '__main__':
    print(__doc__)
    print(solve())
