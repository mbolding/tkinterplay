#!/usr/bin/env python
def trial_division(n):
    a = []
    while n % 2 == 0:
        a.append(2)
        n /= 2
    f = 3

    while f * f <= n:
        if n % f == 0:
            a.append(f)
            n /= f
        else:
            f += 2

    if n != 1:
        a.append(n)

    return a


trial_division(13195)

trial_division(600851475143)

trial_division(2520)
