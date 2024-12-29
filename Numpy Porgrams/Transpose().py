import numpy as np
a=[1,2,3]
print(np.ndim(a))
print(np.shape(a))
print("====================")
c=np.atleast_3d(a)
print(c)
print(np.ndim(a))
print(np.shape(a))
print("===================")
