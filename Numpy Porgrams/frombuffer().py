import numpy as np
x=b"ABCDEFG Manivel"
a=np.frombuffer(x,dtype="S1",count=-1, offset=0).reshape(5,3)
print(a)
print(len(a))
print(a.ndim)
print(a.size)
print(a.shape)
print(a.itemsize)
print(a.nbytes)







