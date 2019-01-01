#!/usr/bin/env python
f = open("e/t13.txt", "r")  # file with nummbers
x = f.readlines()
f.close()
str(sum(map(int, x)))[:10]
