#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Problem 37

The number 3797 has an interesting property. Being prime itself, it is possible
to continuously remove digits from left to right, and remain prime at each
stage: 3797, 797, 97, and 7. Similarly we can work from right to left:
3797, 379, 37, and 3.

Find the sum of the only eleven primes that are both truncatable from left
to right and right to left.

NOTE: 2, 3, 5, and 7 are not considered to be truncatable primes.
'''

from prime import prime_sieve, is_prime


def is_truncatable(num):
    if not is_prime(num):
        return False

    prime = str(num)
    for n in xrange(1, len(prime)):
        if not is_prime(int(prime[:n])):
            return False
        if not is_prime(int(prime[n:])):
            return False

    return True


print sum([n for n in range(10, 800000) if is_truncatable(n)])
