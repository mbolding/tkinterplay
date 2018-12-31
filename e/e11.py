#!/usr/bin/env python

import numpy as np

a = np.loadtxt("e/t11.txt")
b = np.pad(a, 4, "constant")

hmax = np.max(
    np.prod(np.stack([np.roll(b, i, axis=0) for i in range(4)], axis=0), axis=0)
)
hmax

vmax = np.max(
    np.prod(np.stack([np.roll(b, i, axis=1) for i in range(4)], axis=0), axis=0)
)
vmax

drmax = np.max(
    np.prod(
        np.stack([np.roll(np.roll(b, i, axis=1), i, axis=0) for i in range(4)], axis=0),
        axis=0,
    )
)
drmax

dlmax = np.max(
    np.prod(
        np.stack(
            [np.roll(np.roll(b, -i, axis=1), i, axis=0) for i in range(4)], axis=0
        ),
        axis=0,
    )
)
dlmax

# %%

from numpy import *

grid = loadtxt("e/t11.txt")

horiz = max(prod(grid[i, j : j + 4]) for i in range(20) for j in range(17))
vert = max(prod(grid[i : i + 4, j]) for i in range(17) for j in range(20))
d1 = max(prod(diag(grid[i : i + 4, j : j + 4])) for i in range(17) for j in range(17))
d2 = max(
    prod(diag(grid[i : i + 4, j + 4 : j : -1])) for i in range(17) for j in range(17)
)
print(max(horiz, vert, d1, d2))
