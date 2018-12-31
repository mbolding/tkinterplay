#!/usr/bin/env python
def palindrome(start, stop):
    a = []
    for i in range(start, stop):
        s = str(i)
        a.append(int(s + s[::-1]))

    return a[::-1]


P = palindrome(100, 1000)


def divisable(n, start, stop):
    for i in range(stop, start, -1):
        if n % i == 0:
            return i


divisable(9009, 10, 100)


for p in P:
    d = divisable(p, 100, 1000)
    if d:
        q = p / d
        if q < 1000:
            print(p, d, q)
            break
