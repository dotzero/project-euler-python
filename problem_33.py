#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Problem 33

The fraction 49/98 is a curious fraction, as an inexperienced mathematician
in attempting to simplify it may incorrectly believe that 49/98 = 4/8,
which is correct, is obtained by cancelling the 9s.

We shall consider fractions like, 30/50 = 3/5, to be trivial examples.

There are exactly four non-trivial examples of this type of fraction,
less than one in value, and containing two digits in the numerator
and denominator.

If the product of these four fractions is given in its lowest common terms,
find the value of the denominator.
'''

from prime import gcd


def is_curious(xx, yy):
    if xx == yy:
        return False

    x = [float(n) for n in str(xx)]
    y = [float(n) for n in str(yy)]

    if x[1] != y[0] or y[1] == 0:
        return False

    return float(xx) / float(yy) == x[0] / y[1]


curious = [[x, y] for x in xrange(10, 100) for y in xrange(10, 100) if is_curious(x, y)]
m, n = reduce(lambda x, y: [x[0] * y[0], x[1] * y[1]], curious)

print n / gcd(m, n)
