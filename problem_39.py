#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Problem 39

If p is the perimeter of a right angle triangle with integral length sides,
{a,b,c}, there are exactly three solutions for p = 120.

    {20,48,52}, {24,45,51}, {30,40,50}

For which value of p ≤ 1000, is the number of solutions maximised?
'''

from math import sqrt

perimeters = {}
for a in range(1, 1000):
    for b in range(1, int(a / 2) + 1):
        c = sqrt(a ** 2 + b ** 2)
        p = a + b + c
        if c == int(c) and p < 1001:
            perimeters[p] = perimeters.get(p, 0) + 1

inverse = [(value, key) for key, value in perimeters.items()]
print max(inverse)[1]
