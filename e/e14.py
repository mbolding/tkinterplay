#!/usr/bin/env python
def collatz(n):
    a = []
    while n != 1:
        if n % 2 == 0:
            n = int(n / 2)
        else:
            n = 3 * n + 1

        a.append(n)
    return a


def collatz_count(n):
    i = 0
    while n != 1:
        if n % 2 == 0:
            n = int(n / 2)
        else:
            n = 3 * n + 1

        i += 1
    return i


collatz(1)
collatz(2)
collatz(3)

for n in range(1, 20):
    print(n, collatz_count(n), collatz(n))


longest = 0
for n in range(1, int(1e6)):
    collatz_length = collatz_count(n)
    if collatz_length > longest:
        longest = collatz_length
        print(n, "\t", collatz_length)
