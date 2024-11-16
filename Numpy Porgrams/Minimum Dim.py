import numpy as np
a= np.array([1,2,3,4,5,6],dtype=float,ndmin=10,copy=True, order='A',subok=False)
print(a.reshape(3,2))
print(np.ndim(a))
print(a.dtype)
print(a.itemsize)