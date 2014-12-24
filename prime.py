# -*- coding: utf-8 -*-

# Greatest common divisor
def gcd(a, b):
    return gcd(b, a % b) if b else abs(a)


# Least common multiple
def lcm(x, y):
    return x * y / gcd(x, y)


# Determine if a number is prime
def is_prime(n):
    if n < 2:
        return False
    elif n == 2:
        return True
    elif n % 2 == 0:
        return False

    flag = True
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            flag = False
            break
    return flag


# The simple sieve of Eratosthenes
def prime_sieve(n):
    n = int(n)
    primeList = []
    markedList = [False] * (n + 1)

    for i in range(2, n + 1):
        if not markedList[i]:
            primeList.append(i)
            for m in range(i ** 2, n + 1, i):
                markedList[m] = True

    return primeList


# Prime Factorization
def prime_factorization(n, primes=[]):
    limit = int(n ** .5) + 1
    factors = []

    if not primes:
        primes = prime_sieve(limit)

    for p in primes:
        if p > limit: break
        i = 0
        while n % p == 0:
            n //= p
            i += 1
        if i > 0:
            factors.append((p, i));

    if n > 1:
        factors.append((n, 1))

    return factors


# Divisors
def divisors(n):
    factors = prime_factorization(n)
    div = [1]

    for (p, r) in factors:
        div = [d * p ** e for d in div for e in range(r + 1)]

    return sorted(div)


# Proper divisors
def proper_divisors(n):
    return list(divisors(n))[:-1]



