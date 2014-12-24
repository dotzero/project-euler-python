#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Problem 41

We shall say that an n-digit number is pandigital if it makes use of all
the digits 1 to n exactly once. For example, 2143 is a 4-digit pandigital
and is also prime.

What is the largest n-digit pandigital prime that exists?
'''

from prime import prime_sieve

# Determine if a number is pandigital
def is_pandigital(num):
    num = str(num)
    digits = len(num)

    for n in xrange(1, digits + 1):
        if str(n) not in num:
            return False

    return True


primes = prime_sieve(10 ** 7)
print max([n for n in primes[::-1] if is_pandigital(n)])
