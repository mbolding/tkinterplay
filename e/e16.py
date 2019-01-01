#!/usr/bin/env python
def foo(x):
    return sum([int(s) for s in str(x)])


foo(2 ** 15)
foo(2 ** 100)
foo(2 ** 1000)
