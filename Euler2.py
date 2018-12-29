#!/usr/bin/env python
def fib():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b


F = iter(fib())

next(F)
next(F)

F2 = iter(fib())
n = next(F2)

while n < 100:
    n = next(F2)
    print(n)
