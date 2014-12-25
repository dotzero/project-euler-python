#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Problem 43

The number, 1406357289, is a 0 to 9 pandigital number because it is made up
of each of the digits 0 to 9 in some order, but it also has a rather interesting
sub-string divisibility property.

Let d1 be the 1st digit, d2 be the 2nd digit, and so on.
In this way, we note the following:

    d2d3d4=406 is divisible by 2
    d3d4d5=063 is divisible by 3
    d4d5d6=635 is divisible by 5
    d5d6d7=357 is divisible by 7
    d6d7d8=572 is divisible by 11
    d7d8d9=728 is divisible by 13
    d8d9d10=289 is divisible by 17

Find the sum of all 0 to 9 pandigital numbers with this property.
'''

from itertools import permutations


def to_int(nums):
    return int(''.join(map(str, nums)))


def is_interesting(num):
    n = 0
    for d in [2, 3, 5, 7, 11, 13, 17]:
        n = n + 1
        nums = [num[n], num[n + 1], num[n + 2]]
        if not to_int(nums) % d == 0:
            return False

    return True


print sum([to_int(n) for n in permutations(range(10)) if is_interesting(n)])
