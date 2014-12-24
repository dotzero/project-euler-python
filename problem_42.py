#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Problem 42

The nth term of the sequence of triangle numbers is given by,
tn = 1/2*n(n+1); so the first ten triangle numbers are:

    1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

By converting each letter in a word to a number corresponding to its
alphabetical position and adding these values we form a word value. For example,
the word value for SKY is 19 + 11 + 25 = 55 = t10. If the word value is
a triangle number then we shall call the word a triangle word.

Using words.txt, a 16K text file containing nearly two-thousand common English
words, how many are triangle words?
'''

from string import uppercase


def calc_score(word):
    return sum([uppercase.index(n) + 1 for n in word])


triangles = [n * (n + 1) / 2 for n in xrange(1000)]
words = [n.strip('"') for n in open('problem_42_words.txt').read().split(',')]
print len([word for word in words if calc_score(word) in triangles])
