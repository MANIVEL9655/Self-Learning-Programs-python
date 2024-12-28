import numpy as np
a=np.array([2,3,4])
print(a)
print("====================")
print(a.nbytes)
print("====================")
b=np.array([2.0])
print(b.nbytes)
print("====================")
c=a*b
print(c)
print(c.nbytes)
print("====================")
