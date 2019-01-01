#!/usr/bin/env python
import datetime as dt

dt.date(2017, 12, 25).weekday()

num_sun = 0
for year in range(1901, 2001):
    for month in range(1, 13):
        wd = dt.date(year, month, 1).weekday()
        print(year, month)
        if wd == 6:
            print("**")
            num_sun += 1

print(num_sun)
