#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Problem 5

2520 is the smallest number that can be divided by each of the numbers
from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all
of the numbers from 1 to 20?
'''

from prime import lcm

print reduce(lcm, range(2, 20))
