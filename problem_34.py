#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Problem 34

145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.

Find the sum of all numbers which are equal to the sum of the factorial
of their digits.

Note: as 1! = 1 and 2! = 2 are not sums they are not included.
'''

from math import factorial

print sum([n for n in xrange(3, 50000) if
           n == sum([factorial(int(x)) for x in str(n)])])
