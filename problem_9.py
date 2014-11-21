#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Problem 9

A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
    a**2 + b**2 = c**2
For example,
    3**2 + 4**2 = 9 + 16 = 25 = 5**2.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
'''


def triplet(n, m):
    return [
        m ** 2 - n ** 2,
        2 * m * n,
        m ** 2 + n ** 2
    ]


for n in xrange(1, 100):
    for m in xrange(n + 1, 100):
        triple = triplet(n, m)
        if sum(triple) == 1000:
            print reduce(lambda x, y: x * y, triple)
            exit(0)
