#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Problem 50

The prime 41, can be written as the sum of six consecutive primes:

    41 = 2 + 3 + 5 + 7 + 11 + 13

This is the longest sum of consecutive primes that adds to a prime below
one-hundred.

The longest sum of consecutive primes below one-thousand that adds to a prime,
contains 21 terms, and is equal to 953.

Which prime, below one-million, can be written as the sum
of the most consecutive primes?
'''

from prime import prime_sieve

primes = prime_sieve(10 ** 6)
chain = []

for s in range(10):
    seq = primes[s:]
    i = total = 0
    for prime in seq:
        i += 1
        total = total + prime
        if total > 1000000:
            break
        if total in primes:
            c = seq[:i]
            if len(c) > len(chain):
                chain = c

print sum(chain)
