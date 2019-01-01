#!/usr/bin/env python

from scipy.special import comb


def manhattan_paths(n):
    # nope.  return 2 ** n + 2 ** (n - 1)
    return comb((n + n), n, exact=True)


manhattan_paths(20)
