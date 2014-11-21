#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Problem 14

The following iterative sequence is defined for the set of positive integers:

    n → n/2 (n is even)
    n → 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:

    13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1

It can be seen that this sequence (starting at 13 and finishing at 1) contains
10 terms. Although it has not been proved yet (Collatz Problem), it is thought
that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go above one million.
'''

longest = [1, 1]
chains = [0] * (10 ** 6 + 2)


def colatz(n):
    if n == 1:
        return 1
    elif len(chains) > n and not chains[n] == 0:
        return chains[n]
    elif n % 2 == 1:
        return (1 + colatz(n * 3 + 1))
    else:
        return (1 + colatz(n // 2))


for i in xrange(1, 10 ** 6 + 1):
    chains[i] = colatz(i)

    if chains[i] > longest[1]:
        longest = [i, chains[i]]

print 'Collatz(%d) has %d terms' % (longest[0], longest[1])
