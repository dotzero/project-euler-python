#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Problem 35

The number, 197, is called a circular prime because all rotations
of the digits: 197, 971, and 719, are themselves prime.

There are thirteen such primes below 100:
2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97.

How many circular primes are there below one million?
'''

from prime import is_prime


def is_circular(num):
    y = str(num)
    for z in range(0, len(y)):
        n = int(y)
        if not is_prime(n):
            return False
        y = y[-1] + y[0:-1]

    return True


print len([n for n in xrange(3, 1000000, 2) if is_circular(n)]) + 1
