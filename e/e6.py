#!/usr/bin/env python
"""
find sum(1..n)^2 - sum(1^2..n^2) for n = [10, 100]
sum of 1..n is n(n+1)/2
sum of 1^2..n^2 is (n(n + 1)(2n +1))/6
answer = sum squared - sum of squares
"""

# %%
import sympy as sp

sp.init_printing(use_latex="mathjax")

# %%
n = sp.symbols("n")
sum_n = n * (n + 1) / 2
sum_n
sum_squared = sum_n ** 2
sum_squared
sum_of_squares = n * (n + 1) * (2 * n + 1) / 6
sum_of_squares
diff_ss_sos = sum_squared - sum_of_squares
diff_ss_sos
sp.expand(diff_ss_sos)
sp.factor(sp.expand(diff_ss_sos))
diff_ss_sos.subs(n, 10)
diff_ss_sos.subs(n, 100)

# %%
sum([i for i in range(101)]) ** 2 - sum([i ** 2 for i in range(101)])
