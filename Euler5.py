#!/usr/bin/env python

"""
2520 is the smallest number that can be divided by each of the numbers from
1 to 10 without any remainder. What is the smallest positive number that is
evenly divisible by all of the numbers from 1 to 20?
https://projecteuler.net/problem=5
"""
# %%
"""
the answer will be less than 20!
the answer will be the least number in the intersection of the series of
multiples of each number from 1 to 20
"""

from IPython.display import Math


Math(r"lcm < 20!")
Math(r"\{2, 4, 6, 8\dots\}")
Math(r"\prod_{i=1}^{1} a_{i}")
Math(
    r"\{\prod_{i=1}^{1} a_{i} , \prod_{i=1}^{2} a_{i} , \prod_{i=1}^{3} a_{i} , \dots\}"
)

# %%
from IPython.display import Latex

Latex(
    """
    the answer will be less than 20!
    the answer will be the least number in the intersection of the series of
    multiples of each number from 1 to 20

$$lcm < 20!$$

\\begin{equation}
\{\prod_{i=1}^{1} a_{i} , \prod_{i=1}^{2} a_{i} , \prod_{i=1}^{3} a_{i} , \dots\}
\cap
\{\prod_{i=1}^{1} b_{i} , \prod_{i=1}^{2} b_{i} , \prod_{i=1}^{3} b_{i} , \dots\} 


\\end{equation}"""
)

# %%
from functools import reduce  # python 3 moved reduce to functools


def gcd(a, b):
    # Return greatest common divisor using Euclid's Algorithm.
    while b:
        a, b = b, a % b
    return a


def lcm(a, b):
    # Return lowest common multiple.
    return a * b // gcd(a, b)


def lcmm(*args):
    # Return lcm of args.
    return reduce(lcm, args)


# %%
lcmm(*range(1, 11))
