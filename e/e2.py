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


def fibGen(n):
    a, b = 0, 1
    while n > 0:
        yield a
        a, b, n = b, a + b, n - 1


[i for i in fibGen(11)]


def fibGen2(n):
    a, b = 0, 1
    while a < n:
        yield a
        a, b = b, a + b


[k for k in fibGen2(100)]

[k for k in fibGen2(1000)]

[k for k in fibGen2(10000)]


def fibGen3(n):
    a, b = 0, 1
    while a < n:
        yield a
        a, b = b, a + b
        a, b = b, a + b
        a, b = b, a + b


[k for k in fibGen3(1000)]

[k for k in fibGen3(10000)]

[k for k in fibGen3(400000)]

[k for k in fibGen3(4e5)]

[k for k in fibGen3(4e6)]

sum([k for k in fibGen3(4e6)])
