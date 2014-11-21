#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Problem 4

A palindromic number reads the same both ways. The largest palindrome made
from the product of two 2-digit numbers is 9009 = 91  99.
Find the largest palindrome made from the product of two 3-digit numbers.
'''

max = 0

for n1 in xrange(999, 99, -1):
    for n2 in xrange(999, 99, -1):
        c = n1 * n2
        if c > max and str(c) == str(c)[::-1]:
            max = c

print max


