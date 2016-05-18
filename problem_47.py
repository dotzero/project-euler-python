#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Problem 47

The first two consecutive numbers to have two distinct prime factors are:

    14 = 2 × 7
    15 = 3 × 5

The first three consecutive numbers to have three distinct prime factors are:

    644 = 2² × 7 × 23
    645 = 3 × 5 × 43
    646 = 2 × 17 × 19.

Find the first four consecutive integers to have four distinct prime factors. What is the first of these numbers?
'''

from prime import prime_sieve, prime_factorization

primes = prime_sieve(10 ** 4)

n = 1000
c = []

while True:
    n = n + 1
    if len(prime_factorization(n)) == 4:
        c.append(n)
    else:
        del c[:]

    if len(c) == 4:
        print c
        break

