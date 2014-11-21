#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Problem 2

The prime factors of 13195 are 5, 7, 13 and 29.
What is the largest prime factor of the number 600851475143 ?
'''

n = 600851475143
factor = 1

while factor < n:
    # Number is odd, then the factor must be odd (!)
    factor += 2
    while n % factor == 0:
        n /= factor

print factor
