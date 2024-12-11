import numpy as np
a= np.array([1,2,3,4,5,6],dtype=float,ndmin=2,copy=True, order='K',subok=True)
print(a.reshape(3,2))
print(np.ndim(a))
print(a.dtype)
print(a.itemsize)