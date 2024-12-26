import numpy as np
a=np.array(np.arange(10,100,10),dtype="i8")
print(a)
print("++++++++++++++")

a.shape=(3,3)
print(a)
print(len(a))
print(a.size)
print(a.itemsize)
print(a[1:])
print("================")
print(a[2:3])
print("====================")