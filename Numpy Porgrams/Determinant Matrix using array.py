import numpy as np
from numpy.ma.core import arange

a=np.arange(1,5).reshape(2,2)

print(a)
print(a.ndim)
b=np.linalg.det(a)
print(b)