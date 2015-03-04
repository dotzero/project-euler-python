#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Problem 46

It was proposed by Christian Goldbach that every odd composite number
can be written as the sum of a prime and twice a square.

    9 = 7 + 2×1^2
    15 = 7 + 2×2^2
    21 = 3 + 2×3^2
    25 = 7 + 2×3^2
    27 = 19 + 2×2^2
    33 = 31 + 2×1^2

It turns out that the conjecture was false.

What is the smallest odd composite that cannot be written as the sum
of a prime and twice a square?
'''

from prime import prime_sieve

primes = prime_sieve(10 ** 4)
odds = set([n for n in range(3, 10 ** 4, 2)])
composites = list(odds.difference(set(primes)))


def decomposite(n):
    num = 0
    while True:
        num = num + 1
        p = n - (num ** 2) * 2

        if p < 0:
            return False
        elif p in primes:
            return True


for n in composites:
    if not decomposite(n):
        print n
        break
