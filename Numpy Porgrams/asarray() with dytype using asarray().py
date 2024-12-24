import numpy as np
x=[1,2,3,4,5]
print(type(x))
a=np.asarray(x,dtype=float, order="F")
print(type(a))
print(a)
