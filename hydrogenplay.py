# just playing with hydrogen
# https://nteract.gitbooks.io/hydrogen/docs/Usage/GettingStarted.html

# <codecell>
print('Cell', 1)

# <codecell>
print('Cell', 2)

# <codecell>
print('Cell', 3)

# <codecell>
print('Cell', 4)

# <codecell>
print('Cell', 5)

# <codecell>
print('Cell', 6)


# %%

from plotly import offline
offline.init_notebook_mode()

offline.iplot([{"y": [1, 2, 1]}])

# %%
import numpy as np
import matplotlib.pyplot as plt
from plotly import offline as py
py.init_notebook_mode()

t = np.linspace(0, 20, 500)
plt.plot(t, np.sin(t))

py.iplot_mpl(plt.gcf())

# %%
from IPython.display import JSON

data = {"foo": {"bar": "baz"}, "a": 1}
JSON(data)

# %%
import sympy as sp
sp.init_printing(use_latex='mathjax')

x, y, z = sp.symbols('x y z')
f = sp.sin(x * y) + sp.cos(y * z)
sp.integrate(f, x)

# %%
from IPython.display import Math

Math(r'i\hbar \frac{dA}{dt}~=~[A(t),H(t)]+i\hbar \frac{\partial A}{\partial t}.')

# %%
from IPython.display import Latex
Latex('''The mass-energy equivalence is described by the famous equation

$$E=mc^2$$

discovered in 1905 by Albert Einstein.
In natural units ($c$ = 1), the formula expresses the identity

\\begin{equation}
E=m
\\end{equation}''')


# %%
import numpy as np
import pandas as pd

df = pd.DataFrame({'A': 1.,
                   'B': pd.Timestamp('20130102'),
                   'C': pd.Series(1, index=list(range(4)), dtype='float32'),
                   'D': np.array([3] * 4, dtype='int32'),
                   'E': pd.Categorical(["test", "train", "test", "train"]),
                   'F': 'foo'})

df

# %%
import numpy as np

t = np.linspace(0, 20, 500)
t

# %%
from IPython.display import Image
Image('http://jakevdp.github.com/figures/xkcd_version.png')

# %%
import pandas as pd

pd.options.display.html.table_schema = True
pd.options.display.max_rows = None


iris_url = "https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data"

df1 = pd.read_csv(iris_url)

df1

# %%
