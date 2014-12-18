#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Problem 40

An irrational decimal fraction is created by concatenating the positive integers:

    0.12345678910`1`112131415161718192021...

It can be seen that the 12th digit of the fractional part is 1.

If dn represents the n-th digit of the fractional part,
find the value of the following expression.

    d1 × d10 × d100 × d1000 × d10000 × d100000 × d1000000
'''

d = [0] + [int(d) for d in ''.join([str(n) for n in range(1, 1000000)])]
print d[1] * d[10] * d[100] * d[1000] * d[10000] * d[100000] * d[1000000]
