#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Problem 22

Using names.txt, a 46K text file containing over five-thousand first names,
begin by sorting it into alphabetical order. Then working out the alphabetical
value for each name, multiply this value by its alphabetical position in
the list to obtain a name score.

For example, when the list is sorted into alphabetical order, COLIN, which
is worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list. So,
COLIN would obtain a score of 938 × 53 = 49714.

What is the total of all the name scores in the file?
'''

import string


def calc_score(index, name):
    return sum([string.uppercase.index(n) + 1 for n in name]) * index


names = sorted([n.strip('"') for n in open('problem_22_names.txt').read().split(',')])
print sum([calc_score(index + 1, name) for (index, name) in enumerate(names)])
