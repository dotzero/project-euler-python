#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Problem 32

We shall say that an n-digit number is pandigital if it makes use of all
the digits 1 to n exactly once; for example, the 5-digit number, 15234,
is 1 through 5 pandigital.

The product 7254 is unusual, as the identity, 39 × 186 = 7254, containing
multiplicand, multiplier, and product is 1 through 9 pandigital.

Find the sum of all products whose multiplicand/multiplier/product identity
can be written as a 1 through 9 pandigital.

HINT: Some products can be obtained in more than one way so be sure to only
include it once in your sum.
'''


def is_pandigital(x, y):
    num = str(x) + str(y) + str(x * y)
    if not len(num) == 9:
        return False

    for n in xrange(1, 10):
        if str(n) not in num:
            return False

    return True


print sum(set(x * y for x in xrange(1, 5000) for y in xrange(1, 100) if is_pandigital(x, y)))
