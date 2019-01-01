#!/usr/bin/env python

from num2words import num2words

num2words(1)

tot_c = 0
for n in range(1, 1001):
    s = num2words(n).replace("-", "").replace(",", "").replace(" ", "")
    print(len(s), s)
    tot_c += len(s)

tot_c
