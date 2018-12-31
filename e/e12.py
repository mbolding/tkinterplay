#!/usr/bin/env python
# %% define

from functools import reduce


def trinum(n):
    return n * (n + 1) / 2


def factors(n):
    return set(
        reduce(
            list.__add__,
            ([i, n // i] for i in range(1, int(n ** 0.5) + 1) if n % i == 0),
        )
    )


def factors2(n):
    return list(
        reduce(
            list.__add__,
            ([i, n // i] for i in range(1, int(n ** 0.5) + 1) if n % i == 0),
        )
    )


# %% test
x = trinum(3)
[trinum(x) for x in range(10)]
trinums = [trinum(x) for x in range(1, 11)]
[(x, factors(x), len(factors(x))) for x in trinums]
[(x, factors2(x), len(factors2(x))) for x in trinums]

# %% test
x = 2
while True:
    if (len(factors(trinum(x)))) > 5:
        print(trinum(x))
        break
    x += 1

# %% calculate
x = 2
while True:
    if (2 + len(factors(trinum(x)))) > 100:
        print(trinum(x))
        break
    x += 1

# %% calculate
x = 2
while True:
    if (2 + len(factors(trinum(x)))) > 200:
        print(trinum(x))
        break
    x += 1

# %% calculate
x = 2
while True:
    if (2 + len(factors(trinum(x)))) > 300:
        print(trinum(x))
        break
    x += 1

# %% calculate
x = 2
while True:
    if (2 + len(factors(trinum(x)))) > 400:
        print(trinum(x))
        break
    x += 1

# %% calculate
x = 2
while True:
    if (2 + len(factors(trinum(x)))) > 500:
        print(trinum(x))
        break
    x += 1

# %%
import sympy as sp

num_div = 0
tri_num = 0
i = 0
while num_div <= 5:
    i += 1
    tri_num += i
    num_div = sp.divisor_count(tri_num)

print(tri_num)
