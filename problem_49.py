#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Problem 49

The arithmetic sequence, 1487, 4817, 8147, in which each of the terms
increases by 3330, is unusual in two ways: (i) each of the three terms
are prime, and, (ii) each of the 4-digit numbers are permutations
of one another.

There are no arithmetic sequences made up of three 1-, 2-, or 3-digit primes,
exhibiting this property, but there is one other 4-digit increasing sequence.

What 12-digit number do you form by concatenating the three terms
in this sequence?
'''

from prime import prime_sieve, is_prime


def to_int(nums):
    return int(''.join(map(str, nums)))


def to_list(num):
    return sorted([int(x) for x in str(num)])


primes = prime_sieve(10 ** 4)
seq = [n for n in primes if n > 1000]
halfmax = max(seq) / 2

for s in seq:
    for n in range(s, halfmax):
        n2 = s + n
        n3 = s + n * 2
        if is_prime(n2) and is_prime(n3):
            if to_list(s) == to_list(s + n) == to_list(s + n * 2):
                print '%s%s%s' % (s, s + n, s + n * 2)
