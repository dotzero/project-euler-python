#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Problem 7

By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13,
we can see that the 6th prime is 13.

What is the 10 001st prime number?
'''

from prime import prime_sieve

primeList = prime_sieve(200000)
print primeList[10000] # start from 0
