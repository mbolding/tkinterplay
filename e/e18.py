#!/usr/bin/env python
import numpy as np

a = np.loadtxt("e/t18.txt")
np.shape(a)
for r in range(13, -1, -1):
    # print(r, a[r, :])
    for c in range(14):
        if a[r, c] != 0:
            a[r, c] = a[r, c] + max(a[r + 1, [c, c + 1]])

a
