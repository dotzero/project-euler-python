#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Problem 38

Take the number 192 and multiply it by each of 1, 2, and 3:

    192 × 1 = 192
    192 × 2 = 384
    192 × 3 = 576

By concatenating each product we get the 1 to 9 pandigital, 192384576. We will
call 192384576 the concatenated product of 192 and (1,2,3)

The same can be achieved by starting with 9 and multiplying by 1, 2, 3, 4,
and 5, giving the pandigital, 918273645, which is the concatenated product
of 9 and (1,2,3,4,5).

What is the largest 1 to 9 pandigital 9-digit number that can be formed
as the concatenated product of an integer with (1,2, ... , n) where n > 1?
'''


def is_pandigital(num):
    num = str(num)
    if not len(num) == 9:
        return False

    for n in xrange(1, 10):
        if str(n) not in num:
            return False

    return True


maximum = []
for n in xrange(9, 10000):
    num = ''
    for m in xrange(1, 10):
        num += str(n * m)
        if is_pandigital(num):
            maximum.append(num)

print max(maximum)
