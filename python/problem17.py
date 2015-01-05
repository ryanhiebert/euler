#!/usr/bin/env python3

"""Project Euler Problem 17

If the numbers 1 to 5 are written out in words:
one, two, three, four, five,
then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

If all the numbers from 1 to 1000 (one thousand) inclusive were
written out in words, how many letters would be used?


NOTE: Do not count spaces or hyphens. For example, 342 (three hundred
and forty-two) contains 23 letters and 115 (one hundred and fifteen)
contains 20 letters. The use of "and" when writing out numbers is in
compliance with British usage.
"""


def spell(number):
    """Return the words to spell the number."""
    if number > 1000:
        raise  # This doesn't handle numbers greater than 1000

    if number == 1000:
        return ['one', 'thousand']

    if number >= 100:
        if number % 100 == 0:
            return spell(number // 100) + ['hundred']
        else:
            return spell(number // 100 * 100) + ['and'] + spell(number % 100)

    if number >= 20:
        names = {
            20: 'twenty',
            30: 'thirty',
            40: 'forty',
            50: 'fifty',
            60: 'sixty',
            70: 'seventy',
            80: 'eighty',
            90: 'ninety',
        }
        if number % 10 == 0:
            return [names[number]]
        else:
            return spell(number // 10 * 10) + spell(number % 10)

    names = [
        'zero', 'one', 'two', 'three', 'four',
        'five', 'six', 'seven', 'eight', 'nine',
        'ten', 'eleven', 'twelve', 'thirteen', 'fourteen',
        'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen',
    ]
    return [names[number]]


def solve():
    """Solve the problem."""
    return sum(len(''.join(spell(num))) for num in range(1, 1001))


if __name__ == '__main__':
    print(__doc__)
    print(solve())
