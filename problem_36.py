#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Problem 36

The decimal number, 585 = 1001001001 (binary), is palindromic in both bases.

Find the sum of all numbers, less than one million, which are palindromic
in base 10 and base 2.

(Please note that the palindromic number, in either base,
may not include leading zeros.)
'''


def is_palindromic(n):
    b = bin(n)[2:]
    n = str(n)
    return b == b[::-1] and n == n[::-1]


print sum([n for n in xrange(1000000) if is_palindromic(n)])
