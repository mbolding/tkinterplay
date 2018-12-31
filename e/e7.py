#!/usr/bin/env python

import numpy


def primesfrom2to(n):
    # Input n>=6, Returns a array of primes, 2 <= p < n
    sieve = numpy.ones(int(n / 3) + (n % 6 == 2), dtype=numpy.bool)
    for i in range(1, int(int(n ** 0.5) / 3) + 1):
        if sieve[i]:
            k = 3 * i + 1 | 1
            sieve[k * int(k / 3) :: 2 * k] = False
            sieve[k * int((k - 2 * (i & 1) + 4) / 3) :: 2 * k] = False
    return numpy.r_[2, 3, ((3 * numpy.nonzero(sieve)[0][1:] + 1) | 1)]


primesfrom2to(100)

# %%
from itertools import compress


def rwh_primes1v1(n):
    """ Returns  a list of primes < n for n > 2 """
    sieve = bytearray([True]) * (n // 2)
    for i in range(3, int(n ** 0.5) + 1, 2):
        if sieve[i // 2]:
            sieve[i * i // 2 :: i] = bytearray((n - i * i - 1) // (2 * i) + 1)
    return [2, *compress(range(3, n, 2), sieve[1:])]


def rwh_primes1v2(n):
    """ Returns a list of primes < n for n > 2 """
    sieve = bytearray([True]) * (n // 2 + 1)
    for i in range(1, int(n ** 0.5) // 2 + 1):
        if sieve[i]:
            sieve[2 * i * (i + 1) :: 2 * i + 1] = bytearray(
                (n // 2 - 2 * i * (i + 1)) // (2 * i + 1) + 1
            )
    return [2, *compress(range(3, n, 2), sieve[1:])]


rwh_primes1v1(100)
rwh_primes1v2(100)

# %%
import sympy as sp

sp.prime(6)
sp.prime(10001)