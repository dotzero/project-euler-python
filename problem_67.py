#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Problem 67

By starting at the top of the triangle below and moving to adjacent numbers
on the row below, the maximum total from top to bottom is 23.

       3
      7 4
     2 4 6
    8 5 9 3

That is, 3 + 7 + 4 + 9 = 23.

Find the maximum total from top to bottom in triangle.txt, a 15K text file
containing a triangle with one-hundred rows.

NOTE: This is a much more difficult version of Problem 18. It is not possible
to try every route to solve this problem, as there are 2**99 altogether! If you
could check one trillion (10**12) routes every second it would take over twenty
billion years to check them all. There is an efficient algorithm to solve it.
;o)
'''


def get_children(row, index):
    return triangle[row + 1][index], triangle[row + 1][index + 1]


triangle = [[int(n) for n in l.strip().split()] for l in
            open('problem_67_triangle.txt').readlines()]

for row in xrange(len(triangle) - 2, -1, -1):
    for index, value in enumerate(triangle[row]):
        triangle[row][index] = max(
            [value + child for child in get_children(row, index)])

print triangle[0][0]
