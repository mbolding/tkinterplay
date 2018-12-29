#!/usr/bin/env python


def multiplesOf3and5(number):
    total = 0
    for n in range(number):
        if n % 3 == 0:
            total += n
        elif n % 5 == 0:
            total += n

    return total


def multiplesOf3and5b(number):
    total = (
        sum(range(0, number, 3)) + sum(range(0, number, 5)) - sum(range(0, number, 15))
    )
    return total


multiplesOf3and5(10)
multiplesOf3and5(1000)
multiplesOf3and5(49)
multiplesOf3and5(19564)

multiplesOf3and5b(10)
multiplesOf3and5b(1000)
multiplesOf3and5b(49)
multiplesOf3and5b(19564)
